import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('gradient.png', 0)
_, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
_, th2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
_, th3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
_, th4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
_, th5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)

titles = ['Original Image', 'Binary', 'Binary_INV', 'TRUNC', 'TOZERO','TOZERO_INV']
images = [img, th1, th2, th3, th4, th5]
#cv2.imshow('Image', img)
#cv2.imshow('th1', th5)

for i in range(6):
    plt.subplot(2, 3, 1+i), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt. show()

#cv2.waitKey(0)
#cv2.destroyAllWindows()