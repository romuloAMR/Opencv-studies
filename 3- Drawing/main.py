import numpy as np
import cv2 as cv
 
# Create a black image
img = np.zeros((512,512, 3), np.uint8)

cv.line(img, (0,0), (511,511), (255, 255, 255), 2)

cv.circle(img, (256, 256), 50, (255, 255, 255), 2)
cv.circle(img, (256, 256), 25, (255, 255, 255), -1) #-1 to fill the circle 

cv.rectangle(img, (106, 106), (406, 406), (255, 255, 255), 2) #the same logic as for the circle to fill the rectangle

font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img, "OpenCV", (200, 25), font, 1, (255, 255, 255))

cv.imshow("Img", img)
cv.waitKey(0)
cv.destroyAllWindows()