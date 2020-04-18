import cv2
from matplotlib import pyplot as plt

img = cv2.imread('lena.jpg')        #BGR Format
cv2.imshow('image', img)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.imshow(img)
plt.xticks([]), plt.yticks([])      #Coordinates Disappear
plt.show()                          #RBG Format

cv2.waitKey(0)
cv2.destroyAllWindows()