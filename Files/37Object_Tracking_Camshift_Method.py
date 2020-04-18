import numpy as np
import cv2

cap = cv2.VideoCapture('hardcode.mp4', 0)

# take 1st frame
ret1, frame = cap.read()
# setup initial of location
x,y,w,h = 300,200,100,50
track_window = (x,y,w,h)
# setup ROI
roi = frame[y:y+h,x:x+w]
hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv_roi, np.array((0., 60., 32.)), np.array((180., 255., 255)))
roi_hist = cv2.calcHist([hsv_roi], [0], mask, [180], [0,180])
cv2.normalize(roi_hist, roi_hist, 0, 255, cv2.NORM_MINMAX)
# Setup the termination criteria either 10 iteration or move by atleast 1pt
term_crit = (cv2.TERM_CRITERIA_COUNT | cv2.TERM_CRITERIA_EPS, 10, 1)
cv2.imshow('roi', roi)

while True:
    ret, frame = cap.read()
    if ret:

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        dst = cv2.calcBackProject([hsv], [0], roi_hist, [0, 180], 1)
        # apply meanshift to get the new location
        ret, track_window = cv2.CamShift(dst, track_window, term_crit)
        # Draw it on image
        x,y,w,h = track_window
        fianl_img = cv2.rectangle(frame, (x,y), (x+w,y+h), 255, 3)
        cv2.imshow('frame', frame)
        cv2.imshow('final_frame', fianl_img)
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
