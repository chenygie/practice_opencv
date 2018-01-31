import cv2 as cv
import numpy as np

# Create a black image
img = np.zeros((512,512,3),np.uint8)

# Draw a diagonal blue line with thickness of 5px
cv.line(img,(234,234),(511,511),(255,0,0),5)

# Draw a circle
cv.circle(img,(128,128),50,(0,0,255),-1)

# Draw Ellipse

cv.ellipse(img,(256,256),(100,50),0,0,180,255,-1)

pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))
print(pts.shape)
print(pts)
cv.polylines(img,[pts],True,(0,255,255))


font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2,cv.LINE_AA)

font2 = cv.FONT_HERSHEY_PLAIN
cv.putText(img,"test  words",(20,300),font2,4,(0,0,255),2,cv.LINE_AA)

cv.imwrite("text.png",img)