# import cv2 as cv

# cap = cv.VideoCapture("data/video5.mp4")
# while True:
#     ret, frame = cap.read()
#     cv.namedWindow("output", cv.WINDOW_NORMAL)
#     cv.imshow("output",frame)
#     # cv.waitKey(10)
#     if cv.waitKey(1) == ord('q'):
#             break
# cap.release()
# cv.destroyAllWindows()

import cv2
cap = cv2.VideoCapture("data/video5.mp4")
while True:
    cap = cap.set(cv2.CAP_PROP_FPS, 30) 
    ret,frame = cap.read()
    fps = cap.get(cv2.CAP_PROP_FPS)
    print(fps)

    if not ret:
        break
    cv2.namedWindow("frame", cv2.WINDOW_NORMAL)
    cv2.imshow('frame', frame)

    k = cv2.waitKey(2)
    if k == 27:
        break