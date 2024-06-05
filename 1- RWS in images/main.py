import cv2

img = cv2.imread("parakeet.png", 0)

cv2.imshow("Parakeet", img)
k = cv2.waitKey(0)
if k == ord(" "):
    cv2.destroyAllWindows()
elif k == ord("w"):
    cv2.imwrite("parakeet_gray.png", img)
    cv2.destroyAllWindows()