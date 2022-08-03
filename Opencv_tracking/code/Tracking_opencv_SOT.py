import cv2
import sys
# (major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')
# print(cv2.__version__)
# # print(major_ver)
# print(minor_ver)
# if __name__ == '__main__':
    # Set up tracker.
    # Instead of MIL, you can also use
 
tracker_types = ['BOOSTING', 'MIL','KCF', 'TLD', 'MEDIANFLOW', 'CSRT', 'MOSSE']
tracker_type = tracker_types[5]

# if int(major_ver) > 4  and int(minor_ver) > 3:
#     tracker = cv2.cv2.legacy.Tracker_create(tracker_type)
# else:
if tracker_type == 'BOOSTING':
    tracker = cv2.legacy.TrackerBoosting_create()
if tracker_type == 'MIL':
    tracker = cv2.legacy.TrackerMIL_create()
if tracker_type == 'KCF':
    tracker = cv2.legacy.TrackerKCF_create()
if tracker_type == 'TLD':
    tracker = cv2.legacy.TrackerTLD_create()
if tracker_type == 'MEDIANFLOW':
    tracker = cv2.legacy.TrackerMedianFlow_create()
if tracker_type == 'CSRT':
    tracker = cv2.legacy.TrackerCSRT_create()
if tracker_type == 'MOSSE':
    tracker = cv2.legacy.TrackerMOSSE_create()

# Read video
video = cv2.VideoCapture("data/car.mp4")

# Exit if video not opened.
if not video.isOpened():
    print("Could not open video")
    sys.exit()
# Read first frame.
ret, frame = video.read() 
cv2.namedWindow("Tracking", cv2.WINDOW_NORMAL) # show full conner of video      
cv2.imshow("Tracking", frame)

if not ret:
    print('Cannot read video file')
    sys.exit()        
# Define an initial bounding box
bbox = (0, 0, 0, 0)
# Uncomment the line below to select a different bounding box
bbox = cv2.selectROI("Tracking",frame, False) # select ROI from window "tracking"
# Initialize tracker with first frame and bounding box
ok = tracker.init(frame, bbox)
        
while True:
    # Read a new frame
    ok, frame = video.read()
    if not ok:
        break
    # Start timer
    timer = cv2.getTickCount()
    # Update tracker
    ok, bbox = tracker.update(frame)
    # Calculate Frames per second (FPS)
    fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer)
    # Draw bounding box
    if ok:
        # Tracking success
        p1 = (int(bbox[0]), int(bbox[1])) #bbox[0] = x,bbox[1]=y, bbox[2]= with, bbox[3]= height
        p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
        cv2.rectangle(frame, p1, p2, (0,0,255), 5, 1)
    else :
        # Tracking failure
        cv2.putText(frame, "Tracking failure detected", (100,200), cv2.FONT_HERSHEY_SIMPLEX, 2,(0,0,255),8)

    # Display tracker type on frame
    cv2.putText(frame, tracker_type + " Tracker", (100,50), cv2.FONT_HERSHEY_SIMPLEX, 2, (50,170,50),5)

    # Display FPS on frame
    cv2.putText(frame, "FPS : " + str(int(fps)), (100,160), cv2.FONT_HERSHEY_SIMPLEX, 2, (50,170,50), 5)

    # Display result
    cv2.namedWindow("Tracking", cv2.WINDOW_NORMAL)        
    cv2.imshow("Tracking", frame)
    # Exit if ESC pressed
    k = cv2.waitKey(15) & 0xff
    if k == 27 : break
video.release()
cv2.destroyAllWindows()