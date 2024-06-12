import numpy as np
import cv2 as cv

img = cv.imread("parakeet.png")

print("Values of pixel x = 10 and y =10:", img[10,10])
print("Value Blue of pixel x = 10 and y =10:", img.item(10,10,0))
img.itemset((10,10,0), 10)
print("New value Blue of pixel x = 10 and y =10:", img.item(10,10,0))
print("Number of rows, columns, and channels:", img.shape)
print("Image size:", img.size)

head = img[80:165, 65:170]

cv.imshow("Head of parakeet", head)
cv.waitKey(0)
cv.destroyAllWindows()