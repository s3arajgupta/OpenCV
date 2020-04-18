import cv2
import numpy as np

def nothin(x): #CallBack
    print(x)

#Create a black image, a window
cv2.namedWindow('image')    #creates a window of name image

cv2.createTrackbar('cp', 'image', 10, 400, nothin)

switch = 'Color\nGray'
cv2.createTrackbar(switch, 'image', 0 , 1, nothin)

while(1):
    img = cv2.imread('lena.jpg')
    pos = cv2.getTrackbarPos('cp', 'image')
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img, str(pos), (50,150), font, 4, (0,0,255), 3)
    k = cv2.waitKey(1) & 0xFF
    if k==27:
        break

    s = cv2.getTrackbarPos(switch, 'image')

    if s==0:
        pass
    else:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.imshow('image', img)

cv2.destroyAllWindows()