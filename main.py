import cv2
from geometry import *

image = cv2.imread('5warrows.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(
    gray,
    threshold1=80,
    threshold2=160
)
edges = cv2.GaussianBlur(edges, (3,3), 0)

contours, _ = cv2.findContours(edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

centers = findCenters(gray)
circles = findCircles(contours)

maxRadius = min(image.shape[0] / 2, image.shape[1] / 2)


radiiMap = findRadii(centers, circles, maxRadius)
print(radiiMap)
averageRadii = None
radiiCountCutoff = 1
for center in radiiMap.keys():
    cx, cy = center
    radii = radiiMap[center]
    if len(radii) > radiiCountCutoff:
        if averageRadii is None:
            averageRadii = np.array(radii)
        else:
            averageRadii += np.array(radii)
    for radius in radii:
        cv2.circle(image, (int(cx), int(cy)), int(radius), (0,255,0), 2)
averageRadii /= len(averageRadii)

cv2.imshow('Contours', image)
cv2.imwrite('edges.png', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()

