import cv2
import datetime

cap = cv2.VideoCapture(0)
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))   #propNo. = 3
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))

#cap.set(3, 7000)
#cap.set(4, 7000)
#print(cap.get(3))
#print(cap.get(4))

while(cap.isOpened()):  # cap.isOpened() gives if capturing is on
    ret, frame = cap.read()     #ret is boolean
    if ret == True:

        font = cv2.FONT_HERSHEY_SIMPLEX
        datet = str(datetime.datetime.now())
        text = 'Width: '+ str(cap.get(3))+' & Height : '+str(cap.get(4))
        frame = cv2.putText(frame, datet, (10,50), font, 1, (255,255,255), 5, cv2.LINE_AA)
        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
