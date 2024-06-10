import numpy as np
import cv2 as cv

drawing = False
mode = True
ix, iy = -1, -1


def draw(event, x, y, flags, param):
    global ix, iy, drawing, mode

    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    elif event == cv.EVENT_LBUTTONUP:
        drawing = False
        if mode:
            cv.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)
        else:
            radius = int(((x - ix)**2 + (y - iy)**2)**0.5)
            cv.circle(img, (ix, iy), radius, (0, 0, 255), -1)


img = np.zeros((512, 512, 3), np.uint8)
cv.namedWindow("Blackboard")
cv.setMouseCallback("Blackboard", draw)

while True:
    cv.imshow("Blackboard", img)
    key = cv.waitKey(1)
    if key == ord("m"):
        mode = not mode
    if key == ord("q"):
        break

cv.destroyAllWindows()