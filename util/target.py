import cv2
from geometry import *
from arrows import *
from collections import Counter

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
        self.score = 0
        self.numCircles = len(self.radiiMap[self.centers[0]])
        self.targetType = self.getTargetType()
        print(self.targetType)
    def getTargetType(self):
        if (self.numCircles == 11):
            return 'Vegas 1 Spot'
        elif (self.numCircles == 4):
            return 'NFAA 5 Spot'
        elif (len(self.centers) > 1):
            return 'Vegas 3 spot'
        else:
            return 'NFAA 1 Spot'
    def updateScore(self, before, after):
        newArrowPositions = findArrowPositions(before, after, self.centers)
        circlePositions = []
        for position in newArrowPositions:
            circlePositions.append(self.locateInnerCirclePosition(position))
        circlePositionsCounter = Counter(circlePositions)
        print(circlePositionsCounter)
        
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