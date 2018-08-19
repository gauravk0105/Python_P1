#!usr/bin/python

"""
    write in cmd to install opencv
    
    python -m pip install --upgrade pip
    python -m pip install opencv-python
"""

import cv2

cv2.namedWindow("preview")
vc = cv2.VideoCapture(0)

if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False
print "collecting....."    
while rval:
    cv2.imshow("preview", frame)
    rval, frame = vc.read()
    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        break
cv2.destroyWindow("preview")
vc.release()
execfile ('menu.py')
