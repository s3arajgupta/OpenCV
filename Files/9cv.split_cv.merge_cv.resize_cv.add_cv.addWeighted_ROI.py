import cv2
import numpy as np

img = cv2.imread('lena.jpg')
img2 = cv2.imread('orange.jpg')

print(img.shape)
print(img.size)
print(img.dtype)
b,g,r = cv2.split(img)
img = cv2.merge((b,g,r))

#Region of Interest ROI

ball = img[280:340, 330:390]
img[273:333, 100:160] = ball

dst = cv2.add(img, img2)    #Img sizes should match cv2.resize(img, (512, 512)
addweight = cv2.addWeighted(img, .3, img2, .7, 0)

cv2.imshow('image',addweight)
cv2.waitKey(0)
cv2.destroyAllWindows()