import cv2 as cv

img = cv.imread('Photos/cat.jpg')
cv.imshow("Cat Output", img)
cv.waitKey(5000)
