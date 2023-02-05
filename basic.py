import cv2 as cv
import cv2.cv2
import random

img = cv.imread('Photos/lady.jpg')
rotate_img = cv.rotate(img, cv2.cv2.ROTATE_90_CLOCKWISE)
cv.imshow("rotate_image", rotate_img)
resize_img = cv.resize(img, (0, 0), fx=2, fy=2)
cv.imshow("resize_image", resize_img)
cv.imshow("Cat Output", img)
cv.imwrite("rotated.jpg", rotate_img)
cv.waitKey(0)
cv.destroyAllWindows()


