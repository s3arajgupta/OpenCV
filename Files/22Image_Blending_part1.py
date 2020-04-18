import cv2
import numpy as np

apple = cv2.imread('apple.jpg')
orange = cv2.imread('orange.jpg')

apple_orange = np.hstack((apple[:, :256], orange[:,256:]))

#generate guassian py for apple
apple_copy = apple.copy()
gp_apple = [apple_copy]

for i in range(6):
    apple_copy = cv2.pyrDown(apple_copy)
    gp_apple.append(apple_copy)

#generate guassian py for orange
orange_copy = orange.copy()
gp_orange = [orange_copy]

for i in range(6):
    orange_copy = cv2.pyrDown(orange_copy)
    gp_orange.append(orange_copy)

#laplacian pyd for apple
apple_copy = gp_apple[5]
lp_apple = [apple_copy]

for i in range(5, 0, -1):
    guassian_extented = cv2.pyrUp(gp_apple[i])
    laplacian = cv2.subtract(gp_apple[i-1], guassian_extented)
    lp_apple.append((laplacian))

#placian pyd for orange
orange_copy = gp_orange[5]
lp_orange = [orange_copy]

for i in range(5, 0, -1):
    guassian_extented = cv2.pyrUp(gp_orange[i])
    laplacian = cv2.subtract(gp_orange[i - 1], guassian_extented)
    lp_orange.append((laplacian))

# joing two half
apple_orange_pyd = []
n=0
for apple_lap, orange_lap in zip(lp_apple, lp_orange):
    n += 1
    cols, rows, ch = apple_lap.shape
    laplacian = np.hstack((apple_lap[:, 0:int(cols/2)], orange_lap[:, int(cols/2):]))
    apple_orange_pyd.append(laplacian)

#now reconstruct
apple_orange_resconstruct = apple_orange_pyd[0]
for i in range(1, 6):
    apple_orange_resconstruct = cv2.pyrUp(apple_orange_resconstruct)
    apple_orange_resconstruct = cv2.add(apple_orange_pyd[i], apple_orange_resconstruct)


cv2.imshow('apple_orange', apple_orange_resconstruct)

cv2.waitKey(0)
cv2.destroyAllWindows()