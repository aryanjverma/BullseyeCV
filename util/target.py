import cv2
from geometry import *
from arrows import *
import numpy as np
from targetTypes import TARGET_SPECS
import functools
from crop import crop

@functools.total_ordering
class Target:
    def __init__(self, targetType):
        self.targetType = targetType
        # Use centers and radii directly from the targetType
        self.centers = targetType.centers if isinstance(targetType.centers, list) else targetType.centers.tolist()
        self.numTargets = len(self.centers)
        self.radii = targetType.radii
        self.numCircles = len(self.radii)
        self.score = 0
        self.xCount = 0
        
    def __eq__(self, other):
        if not isinstance(other, Target):
            raise TypeError('Comparing target to non-target is illegal')
        if self.targetType != other.targetType:
            raise TypeError('Comparing differnt target types is illegal')
        return self.score == other.score and self.xCount == other.xCount
    def __lt__(self, other):
        return self.score < other.score or (self.score == other.score and self.xCount < other.xCount)

    # getTargetType is no longer needed since type is passed in constructor
    def updateScore(self, before, after):
        # Use self.centers for arrow detection
        before = crop(before)
        after = crop(after)
        newArrowPositions = findArrowPositions(before, after, self.centers)
        circlePositions = np.zeros(shape=(self.numCircles+1))
        for position in newArrowPositions:
            circlePositions[self.locateInnerCirclePosition(position)] += 1
        self.score += np.dot(circlePositions, self.targetType.scoreVector)
        self.xCount += circlePositions[0]
        
    def locateInnerCirclePosition(self, position):
        for center in self.centers:
            distance = math.sqrt((position[0] - center[0]) ** 2 + (position[1] - center[1]) ** 2)
            if self.radii[self.numCircles - 1] > distance:
                count = 0
                while (count < len(self.radii) and self.radii[count] < distance):
                    count += 1
                return count
        return self.numCircles