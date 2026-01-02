import cv2
import math

image = cv2.imread('hd.webp')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(
    gray,
    threshold1=80,
    threshold2=160
)
edges = cv2.GaussianBlur(edges, (5,5), 0)

contours, hierarchy = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
sizeCutoff = 50
print(hierarchy)
def contourDepth(hierarchy, index):
    depth = 0
    current = index
    while hierarchy[0][current][3] != -1:
        depth += 1
        current = hierarchy[0][current][3]
    return depth
def findNDeepest(hierarchy, N):
    depths = []
    for index in range(len(hierarchy[0])):
        if hierarchy[0][index][2] == -1:
            depth = contourDepth(hierarchy, index)
            depths.append((depth, index))
    depths.sort(key=lambda x: x[0], reverse=True)
    deepestDepths = []
    for index in range(N):
        deepestDepths.append(depths[index][1])
    return deepestDepths
def findCenter(contour):
    M = cv2.moments(contour)
    if M['m00'] != 0:
        cx = M['m10'] / M['m00']
        cy = M['m01'] / M['m00']
        return (cx, cy)
deepestIndeces = findNDeepest(hierarchy, 1)
print(deepestIndeces)
centers = []
for i in deepestIndeces:
    cx, cy = findCenter(contours[i])
    print(cx, cy)
    centers.append((cx, cy))
    cv2.circle(image, (int(cx), int(cy)), 4, (0, 255, 0), 1)
circularityCutoff = 0.8
areaMin = 1000
areaMax = 700000
circles = []
for contour in contours:
    area = cv2.contourArea(contour)
    perimeter = cv2.arcLength(contour, True)
    if perimeter != 0:
        circularity = (4 * math.pi * area) / (perimeter**2)
        if circularity > circularityCutoff and areaMin < area < areaMax:
            circles.append(cv2.minEnclosingCircle(contour))
distanceCutoff = 20
radiusCutoff = 20
centerRadiiMap = dict()
for center in centers:
    cx, cy = center
    radiiSums = []
    radiiCounts = []
    for circle in circles:
        (x, y), r = circle
        if abs(cx - x) < distanceCutoff and abs(cy - y) < distanceCutoff:
            needToAdd = True
            for index in range(len(radiiSums)):
                if abs(radiiSums[index] - r) < radiusCutoff:
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
    centerRadiiMap[(cx, cy)] = radii
for center in centerRadiiMap.keys():
    cx, cy = center
    radii = centerRadiiMap[center]
    for radius in radii:
        cv2.circle(image, (int(cx), int(cy)), int(radius), (0, 255, 0), 2)
print(centerRadiiMap)
print(radii)
print(cx, cy)
cv2.imshow('Contours', image)
cv2.imshow('edges', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()

