import cv2
import numpy as np

img1 = np.zeros((512,512,3), np.uint8)
img1 = cv2.rectangle(img1, (128,0), (384,128), (255,255,255), -1)
img2 = cv2.rectangle(img1, (256,0), (512,512), (255,255,255), -1)

bitAnd = cv2.bitwise_and(img1, img2)
bitOr = cv2.bitwise_or(img1, img2)
bitXor = cv2.bitwise_xor(img1, img2)
bitNot = cv2.bitwise_not(img1)

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
#cv2.imshow('and', bitAnd)
#cv2.imshow('or', bitOr)
#cv2.imshow('xor', bitXor)
#cv2.imshow('not', bitNot)

cv2.waitKey(0)
cv2.destroyAllWindows()