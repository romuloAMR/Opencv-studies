import numpy as np 
import cv2 as cv

def nothing(value):
    pass

img = np.zeros((512, 512, 3), np.uint8)
cv.namedWindow("Board")

cv.createTrackbar("R", "Board", 0, 255, nothing)
cv.createTrackbar("G", "Board", 0, 255, nothing)
cv.createTrackbar("B", "Board", 0, 255, nothing)
cv.createTrackbar("Show", "Board", 0, 1, nothing)

while True:
    cv.imshow("Board", img)

    key = cv.waitKey(1)
    if key == ord("q"):
        break

    r = cv.getTrackbarPos("R", "Board")
    g = cv.getTrackbarPos("G", "Board")
    b = cv.getTrackbarPos("B", "Board")
    show = cv.getTrackbarPos("Show", "Board")

    if show:
        img[:] = [b, g, r]
    else:
        img[:] = [0, 0, 0]

cv.destroyAllWindows()