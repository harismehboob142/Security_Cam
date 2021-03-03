import cv2 as c
import winsound as ws
cam = c.VideoCapture(0)
while cam.isOpened():
    ret, frame = cam.read()
    ret, frame2 = cam.read()
    diff = c.absdiff(frame,frame2)
    gray = c.cvtColor(diff,c.COLOR_BGR2GRAY)
    blur = c.GaussianBlur(gray, (5,5),0)
    _, thresh = c.threshold(blur,20,255,c.THRESH_BINARY)
    dilated = c.dilate(thresh, None, iterations=3)
    contours, _ = c.findContours(dilated,c.RETR_TREE,c.CHAIN_APPROX_SIMPLE)
    # c.drawContours(frame,contours,-1,(0,255,0),2)
    for i in contours:
        if c.contourArea(i) < 5000:
            continue
        x,y,w,h = c.boundingRect(i)
        c.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)
        ws.Beep(800,300)
    if c.waitKey(10) == ord('q'):
        break
    c.imshow('Security Camera',frame)
