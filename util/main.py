import cv2
from target import Target

start = cv2.imread('actualbefore.png')
target = Target(start)
next = cv2.imread('actualAfter.png')
target.updateScore(start, next)
