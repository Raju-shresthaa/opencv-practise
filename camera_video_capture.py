import cv2.cv2
import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)
while True:
    isTrue, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))
    image = np.zeros(frame.shape, np.uint8)

    small_frame = cv.resize(frame, (0, 0), fx=0.5, fy=0.5)
    image[:height // 2, :width // 2] = small_frame
    image[height // 2:, :width // 2] = small_frame
    image[:height // 2, width // 2:] = small_frame
    image[height // 2:, width // 2:] = small_frame
    cv.imshow("Output Video", image)
    print(width)
    if cv.waitKey(1) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
