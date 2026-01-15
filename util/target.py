import cv2
from geometry import *
from arrows import *
import numpy as np
from targetTypes import TARGET_SPECS
import functools

@functools.total_ordering
class Target:
    def __init__(self, start):
        self.start = start
        self.grayStart = cv2.cvtColor(self.start, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(
            self.grayStart,
            threshold1=80,
            threshold2=160
        )
        edges = cv2.GaussianBlur(edges, (3,3), 0)
        contours, _ = cv2.findContours(edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        centers = findCenters(self.grayStart)
        circles = findCircles(contours)
        maxRadius = min(self.start.shape[0] / 2, self.start.shape[1] / 2)
        self.radiiMap = findRadii(centers, circles, maxRadius)
        self.centers = list(self.radiiMap.keys())
        self.numTargets = len(self.centers)
        self.score = 0
        self.numCircles = len(self.radiiMap[self.centers[0]])
        self.targetType = self.getTargetType()
        self.xCount = 0
        print(self.targetType)
    def __eq__(self, other):
        if not isinstance(other, Target):
            raise TypeError('Comparing target to non-target is illegal')
        if self.targetType != other.targetType:
            raise TypeError('Comparing differnt target types is illegal')
        return self.score == other.score and self.xCount == other.xCount
    def __lt__(self, other):
        return self.score < other.score or (self.score == other.score and self.xCount < other.xCount)

    def getTargetType(self):
        for target in TARGET_SPECS:
            if (target.numTargets == self.numTargets and target.numCircles == self.numCircles):
                return target
        raise NotImplementedError('Arrow type of: ' + str(self.numCircles) + ' rings(s) and ' +
                                  str(self.numTargets) + ' spot(s) is not supported.')
    def updateScore(self, before, after):
        newArrowPositions = findArrowPositions(before, after, self.centers)
        circlePositions = np.zeros(shape=(self.numCircles+1))
        for position in newArrowPositions:
            circlePositions[self.locateInnerCirclePosition(position)] += 1
        self.score += np.dot(circlePositions, self.targetType.scoreVector)
        print(self.score)
        self.xCount += circlePositions[0]
        
    def locateInnerCirclePosition(self, position):
        for center in self.centers:
            radii = self.radiiMap[center]
            distance = math.sqrt((position[0]- center[0]) ** 2 + (position[1] - center[1]) ** 2)
            if radii[self.numCircles - 1] > distance:
                count = 0
                while (count < len(radii) and radii[count] < distance):
                    count += 1
                return count
        return self.numCircles