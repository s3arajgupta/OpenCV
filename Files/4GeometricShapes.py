import numpy as np
import cv2

#img = cv2.imread('lena.jpg', 1)
img = np.zeros([512, 512, 3], np.uint8)
img = cv2.line(img, (0,0), (255,255), (255,255,0), 10)
img = cv2.arrowedLine(img, (0,255), (255,255), (255,255,0), 10)

img = cv2.rectangle(img, (10,10), (300,300), (0,0,255), 1)  #-ve valuetofill
img = cv2.circle(img, (400,400), 100, (0,255,0), -1)
font = cv2.FONT_HERSHEY_DUPLEX
img = cv2.putText(img, 'OpenCV', (100,400), font, 3, (255,255,255), 10, cv2.LINE_AA)

cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()