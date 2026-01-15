import cv2
from geometry import *
import math

def findArrowPositions(before, after, centers):
    
    image = cv2.absdiff(before, after)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    _, thresh = cv2.threshold(gray, 40, 255, cv2.THRESH_BINARY)

    contours, _ = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(thresh, contours, -1, (0,255,0), 2)
    contours, _ = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(image, contours, -1, (0,255,0), 2)
    cx, cy = centers[0]
    print(cx, cy)
    areaMin = 50
    positions = []
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > areaMin:
            minDistance = image.shape[0] * 10
            position = (0, 0)
            for contour_point in contour:
                x, y = contour_point[0]
                distance = math.sqrt((cx - x) ** 2 + (cy - y) ** 2)
                if distance < (minDistance):
                    minDistance = distance
                    position = (x, y)
            positions.append(position)
    cv2.imwrite('diff.png', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return positions