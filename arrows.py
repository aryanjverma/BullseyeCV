import cv2
from geometry import *

image = cv2.imread('warrows.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 127, 255, 0)

contours, _ = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(image, contours, -1, (0,255,0), 2)

cv2.imwrite('edges.png', thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()