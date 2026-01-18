import cv2
from target import Target
from targetTypes import *
from crop import crop
target = Target(TARGET_SPECS[3])
start = cv2.imread('nfaa-start.png')
next = cv2.imread('nfaa1-round1.png')
target.updateScore(start, next)
print(target.score)
