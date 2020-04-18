import cv2
from matplotlib import pyplot as plt
import numpy as np

img = cv2.imread('lena.jpg')
layer = img.copy()
gp = [layer]

for i in range(6):
    layer = cv2.pyrDown(layer)
    gp.append(layer)
#    cv2.imshow(str(i), layer)
#lr1 = cv2.pyrDown(img)
#lr2 = cv2.pyrDown(lr1)
#hr1 = cv2.pyrUp(img)
#cv2.imshow("pyrDown1", lr1)
#cv2.imshow("pyrDown2", lr2)
#cv2.imshow("pyrUp1", hr1)           #information is loosed

layer = gp[5]
cv2. imshow('upper level of gaussian pyramid', layer)
lp = [layer]

for i in range(5,0,-1):
    guassian_extended = cv2.pyrUp(gp[i])
    laplacian = cv2.subtract(gp[i-1], guassian_extended)
    cv2.imshow(str(i), laplacian)

cv2.waitKey(0)
cv2.destroyAllWindows()