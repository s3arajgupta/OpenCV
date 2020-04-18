import cv2

cap = cv2.VideoCapture(0)
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))   #propNo. = 3
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))

cap.set(3, 7000)
cap.set(4, 7000)

print(cap.get(3))
print(cap.get(4))


while(cap.isOpened()):  # cap.isOpened() gives if capturing is on
    ret, frame = cap.read()     #ret is boolean
    if ret == True:

        grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
