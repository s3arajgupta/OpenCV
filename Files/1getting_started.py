import cv2

img = cv2.imread('lena.jpg', 1)

print(img)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('lena_copy.png', img)