import cv2
from geometry import *
import numpy as np

def crop(image, contours=None):
    if contours is None:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, threshold1=80, threshold2=160)
        edges = cv2.GaussianBlur(edges, (3, 3), 0)
        contours, _ = cv2.findContours(edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    sourcePoints = findLargestSquare(contours, image.shape)
    if sourcePoints is None:
        h, w, _ = image.shape
        sourcePoints = np.array([[0,0], [w - 1, 0], [w - 1, h - 1], [0, h - 1]], dtype="float32")
    else:
        sourcePoints = orderPoints(sourcePoints)
    
    W, H = 1000, 1000
    destinationPoints = np.array([
        [0, 0],
        [W - 1, 0],
        [W - 1, H - 1],
        [0, H - 1]
    ], dtype="float32")
    T = cv2.getPerspectiveTransform(sourcePoints, destinationPoints)
    warped = cv2.warpPerspective(image, T, (W, H))
    return warped