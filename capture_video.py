import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)

while(True):
    #Capture frame by frame
    ret,frame = cap.read()

    # operations on the frame come here
    gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)

    # display the resulting frame
    cv.imshow('frame',gray)
    if cv.waitKey(1) & 0xff == ord('q'):
        break
# release the capture
cap.release()
cv.destroyAllWindows()