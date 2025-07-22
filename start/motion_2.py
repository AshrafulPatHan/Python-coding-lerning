import pandas as pd
import cv2
from datetime import datetime
from collections import deque

# Initialize variables
initialState = None
motionTrackList = deque([None, None], maxlen=2)
motionTime = []
dataFrame = pd.DataFrame(columns=["Initial", "Final"])

# Start webcam capture
video = cv2.VideoCapture(0)

while True:
    check, cur_frame = video.read()
    if not check:
        break  # Exit if no frame is captured

    var_motion = 0
    gray_frame = cv2.GaussianBlur(cv2.cvtColor(cur_frame, cv2.COLOR_BGR2GRAY), (21, 21), 0)

    if initialState is None:
        initialState = gray_frame
        continue

    # Compute frame difference and threshold
    differ_frame = cv2.absdiff(initialState, gray_frame)
    thresh_frame = cv2.dilate(cv2.threshold(differ_frame, 30, 255, cv2.THRESH_BINARY)[1], None, iterations=2)

    # Detect contours
    contours, _ = cv2.findContours(thresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    for cur in contours:
        if cv2.contourArea(cur) < 10000:
            continue
        var_motion = 1
        x, y, w, h = cv2.boundingRect(cur)
        cv2.rectangle(cur_frame, (x, y), (x + w, y + h), (0, 255, 0), 3)

    # Track motion status
    motionTrackList.append(var_motion)

    if motionTrackList[-1] == 1 and motionTrackList[-2] == 0:
        motionTime.append(datetime.now())

    if motionTrackList[-1] == 0 and motionTrackList[-2] == 1:
        motionTime.append(datetime.now())

    # Display frames
    cv2.imshow("Gray Frame", gray_frame)
    cv2.imshow("Difference Frame", differ_frame)
    cv2.imshow("Threshold Frame", thresh_frame)
    cv2.imshow("Color Frame", cur_frame)

    if cv2.waitKey(1) == ord('m'):
        if var_motion == 1:
            motionTime.append(datetime.now())
        break

# Store motion times in DataFrame
if len(motionTime) % 2 != 0:
    motionTime.append(datetime.now())

time_records = [{"Initial": motionTime[i], "Final": motionTime[i+1]} for i in range(0, len(motionTime), 2)]
dataFrame = pd.DataFrame(time_records)

# Save to CSV
dataFrame.to_csv("EachMovement.csv", index=False)

# Cleanup
video.release()
cv2.destroyAllWindows()
