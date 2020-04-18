import cv2
from matplotlib import pyplot as plt
import numpy as np

img = cv2.imread('lena.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

kernal = np.ones((5, 5), np.float32)/25
dst = cv2.filter2D(img, -1, kernal)
blur = cv2.blur(img, (5,5))
gaussian = cv2.GaussianBlur(img, (5, 5), 0) #weight
median = cv2.medianBlur(img, 3)           #salt & pepper
bilaterl = cv2.bilateralFilter(img, 9, 75, 75)    #preserve edges


titles = ['images', '2dConv', 'blur','gaussian', 'median', 'bilaterl']
images = [img, dst, blur, gaussian, median, bilaterl]

for i in range(6):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])


plt.show()