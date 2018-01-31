import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)

# define the codec and create VideoWriter object

fourcc = cv.VideoWriter_fourcc(*'DIVX')
size = (int(cap.get(cv.CAP_PROP_FRAME_WIDTH)),int(cap.get(cv.CAP_PROP_FRAME_HEIGHT)))
out = cv.VideoWriter('test3.mov',fourcc,20,size)
while(cap.isOpened()):
    ret,frame = cap.read()
    if ret==True:
        frame = cv.flip(frame,0)

        # write the flipped frame
        out.write(frame)

        cv.imshow('frame',frame)
        if cv.waitKey(1) & 0xff == ord('q'):
            break
    else:
        break
# Release everything if job is finished

cap.release()
out.release()
cv.destroyAllWindows()
