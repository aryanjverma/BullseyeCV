import cv2
import numpy as np
import math

def findCenters(gray):
    rows = gray.shape[0]
    minRadius = 50
    maxRadius = 150
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, rows / 8,
                                param1=100, param2=50,
                                minRadius=minRadius, maxRadius=maxRadius)
    centers = []
    if circles is not None:
        circles = np.uint16(np.around(circles))
        for circle in circles[0, :]:
            centers.append((circle[0], circle[1]))
    return centers

circularityCutoff = 0.75
areaMin = 10
def findCircles(contours):
    circles = []
    for contour in contours:
        area = cv2.contourArea(contour)
        perimeter = cv2.arcLength(contour, True)
        if perimeter != 0:
            circularity = (4 * math.pi * area) / (perimeter**2)
            if circularity > circularityCutoff and areaMin < area:
                circles.append(cv2.minEnclosingCircle(contour))
    return circles

distanceCutoff = 20
radiusCutoff = 10
radiiCountCutoff = 1
def findRadii(centers, circles, maxRadius):
    centerRadiiMap = dict()
    for center in centers:
        cx, cy = center
        radiiSums = []
        radiiCounts = []
        for circle in circles:
            (x, y), r = circle
            if abs(cx - x) < distanceCutoff and abs(cy - y) < distanceCutoff and radiusCutoff < r < maxRadius:
                needToAdd = True
                for index in range(len(radiiSums)):
                    if abs(radiiSums[index] / radiiCounts[index] - r) < radiusCutoff:
                        radiiSums[index] += r
                        radiiCounts[index] += 1
                        needToAdd = False
                        break
                if needToAdd:
                    radiiSums.append(r)
                    radiiCounts.append(1)
        radii = []
        for index in range(len(radiiCounts)):
            radii.append(radiiSums[index] / radiiCounts[index])
        if (len(radii) > radiiCountCutoff):
            centerRadiiMap[(cx, cy)] = radii
    return centerRadiiMap
