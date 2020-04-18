import cv2
import numpy as np

img = cv2.imread('messi5.jpg')
greyimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
temp = cv2.imread('messi5Template.jpg', 0)
w, h = temp.shape[::-1]

res = cv2.matchTemplate(greyimg, temp, cv2.TM_CCOEFF_NORMED)
print(res)
thresh = 0.9    
loc = np.where(res >= thresh)
print(loc)

for pt in zip(*loc[::-1]):
    cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)

cv2.imshow('img', img)

cv2.waitKey(0)
cv2.destroyAllWindows()