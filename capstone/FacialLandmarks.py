from imutils import face_utils
import imutils
import numpy as np
import argparse
import time
import datetime
from imutils.video import VideoStream
import dlib
import cv2

# creates argument parser
ap = argparse.ArgumentParser()
ap.add_argument("-p", "--shape-predictor", required = True, help = "path to facial landmark detector")
args = vars(ap.parse_args())

# initializes dlib face detector and creates landmark predictor
print("[INFO] loading facial landmark predictor...")
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(args["shape_predictor"])

# creates video stream from webcam
video = VideoStream(0).start()
time.sleep(2.0)

while True:
    # grabs frame, resizes, and converts to grayscale
    frame = video.read()
    frame = imutils.resize(frame, width=640)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # detects faces in grayscale frame
    rects = detector(gray, 0)
    # loops for face detection
    for rect in rects:
        # determines facial landmarks and converts coordinates to numpy array
        shape = predictor(gray, rect)
        shape = face_utils.shape_to_np(shape)

        # loop over facial landmark coordinates and draw them on image
        for (x, y) in shape:
            cv2.circle(frame, (x, y), 1, (0, 0, 255), -1)

    # show output image w/ face detections and landmarks
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):
        break

cv2.destroyAllWindows()
video.stop()
