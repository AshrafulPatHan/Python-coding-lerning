# import cv2
# import numpy as np
# from datetime import datetime
# from collections import deque

# # Constants
# MOTION_THRESHOLD = 10000  # Minimum contour area to detect motion
# GAUSSIAN_BLUR_SIZE = (21, 21)  # Kernel size for Gaussian blur
# THRESHOLD_VALUE = 30  # Threshold value for binary thresholding
# DILATION_ITERATIONS = 2  # Number of iterations for dilation
# FRAME_WIDTH = 640  # Desired frame width
# FRAME_HEIGHT = 480  # Desired frame height
# BLUE_COLOR = (255, 0, 0)  # BGR format for blue color

# # Initialize variables
# motion_track = deque([None, None], maxlen=2)
# motion_times = []

# # Start webcam capture
# video = cv2.VideoCapture(0)
# video.set(cv2.CAP_PROP_FRAME_WIDTH, FRAME_WIDTH)
# video.set(cv2.CAP_PROP_FRAME_HEIGHT, FRAME_HEIGHT)

# def process_frame(frame):
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     gray = cv2.GaussianBlur(gray, GAUSSIAN_BLUR_SIZE, 0)
#     return gray

# while True:
#     ret, frame = video.read()
#     if not ret:
#         break  # Exit if no frame is captured

#     gray_frame = process_frame(frame)

#     # Compute frame difference and threshold
#     if 'prev_gray_frame' in locals():
#         diff_frame = cv2.absdiff(prev_gray_frame, gray_frame)
#         _, thresh_frame = cv2.threshold(diff_frame, THRESHOLD_VALUE, 255, cv2.THRESH_BINARY)
#         thresh_frame = cv2.dilate(thresh_frame, None, iterations=DILATION_ITERATIONS)

#         # Detect contours
#         contours, _ = cv2.findContours(thresh_frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#         motion_detected = any(cv2.contourArea(contour) >= MOTION_THRESHOLD for contour in contours)

#         # Draw blue rectangles to cover detected motion
#         if motion_detected:
#             for contour in contours:
#                 if cv2.contourArea(contour) >= MOTION_THRESHOLD:
#                     x, y, w, h = cv2.boundingRect(contour)
#                     cv2.rectangle(frame, (x, y), (x + w, y + h), BLUE_COLOR, -1)  # Solid blue box

#         # Track motion status
#         motion_track.append(motion_detected)

#         # Record motion start and end times
#         if motion_track[-1] and not motion_track[-2]:
#             motion_times.append(datetime.now())
#         elif not motion_track[-1] and motion_track[-2]:
#             motion_times.append(datetime.now())

#     # Update previous frame
#     prev_gray_frame = gray_frame

#     # Display frames
#     cv2.imshow("Gray Frame", gray_frame)
#     cv2.imshow("Difference Frame", diff_frame if 'diff_frame' in locals() else np.zeros_like(gray_frame))
#     cv2.imshow("Threshold Frame", thresh_frame if 'thresh_frame' in locals() else np.zeros_like(gray_frame))
#     cv2.imshow("Motion Covered (Blue Box)", frame)

#     # Exit on 'm' key press
#     if cv2.waitKey(1) == ord('m'):
#         if motion_detected:
#             motion_times.append(datetime.now())
#         break

# # Ensure motion times are paired
# if len(motion_times) % 2 != 0:
#     motion_times.append(datetime.now())

# # Cleanup
# video.release()
# cv2.destroyAllWindows()
