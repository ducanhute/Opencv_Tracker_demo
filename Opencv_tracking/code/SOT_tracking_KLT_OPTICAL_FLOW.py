import cv2 as cv
import numpy as np
import time

cap = cv.VideoCapture('data/plane.mp4')
# filename -> video clip
# 0,1 -> camera
if not cap.isOpened():
    print('can not open video clip/camera')
    exit()
# load first frame
ret,prevImage = cap.read()
prevImage_gray = cv.cvtColor(prevImage, cv.COLOR_BGR2GRAY)
cv.namedWindow("Tracking", cv.WINDOW_NORMAL) # show full conner of video      
cv.imshow("Tracking", prevImage) # show full coner of first fram to selecROI
# detect object -> bounding box -> roi
     # detect object bang chuot# khau nay de bo thuat toan detect object 
        #dau ra la toa do diem cua bounding box
x,y,w,h = cv.selectROI("Tracking",prevImage,False) # detect object bang chuot# khau nay de bo thuat toan detect object
roi = prevImage_gray[y:y+h, x:x+w]
# determine key points in the roi
kp0 = cv.goodFeaturesToTrack(roi,30,0.01,1)
print(kp0)
# chuyen kp0 ve toa do goc cua tam anh ban dau, toa do hien tai la cua bounding box
for i in kp0:
    i[0,0] = i[0,0] + x
    i[0,1] = i[0,1] + y

# fps = 12
# prev = 0
while True:
    # time_elapsed = time.time() - prev
    # if time_elapsed > 1./fps:
    #     prev = time.time()
        # read frame by frame
        ret, frame = cap.read()
         ## Start timer
        timer = cv.getTickCount()
        if not ret:
            print(' can not read video frame. Video ended?')
            break
        nextImage = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        # calculate optical flow
        kp1, status, erro = cv.calcOpticalFlowPyrLK(prevImage_gray, nextImage, kp0, None)
        
        # draw key points,kp1: float--> chuyen ve int
        for point in kp1:
            xp = int(point[0,0])
            yp = int(point[0,1])
            cv.circle(frame,(xp,yp), 5, (0,0,255), 3)
        # drawing bounding box around series of point in kp1
        x,y,w,h = cv.boundingRect(kp1)
        cv.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 10)
        # update keypoints
        kp0 = kp1
        prevImage_gray = nextImage
        # Calculate Frames per second (FPS)
        fps = cv.getTickFrequency() / (cv.getTickCount() - timer)
        # Display FPS on frame
        cv.putText(frame, "FPS : " + str(int(fps)), (100,250), cv.FONT_HERSHEY_SIMPLEX, 3, (0,0,255), 5)
        cv.putText(frame,"Optical Flow",(100,100),cv.FONT_HERSHEY_COMPLEX,3,(0,0,255),5)
        #show frame
        cv.namedWindow("Tracking", cv.WINDOW_NORMAL) # if opencv donot show full conner of video this code will h
        cv.imshow('Tracking', frame)
        # close clip
        if cv.waitKey(1) == ord('q'):
            break
cap.release()
cv.destroyAllWindows()
# nhuoc diem khi object bi che se xuat hien loi khi tracking