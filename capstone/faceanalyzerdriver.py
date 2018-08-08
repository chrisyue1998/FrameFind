# import the necessary packages
from __future__ import print_function
from faceanalyzer import FaceAnalyzerGUI
from imutils.video import VideoStream
import argparse
import time

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-o", "--output", required=True,
                help="path to output directory to store snapshots")
args = vars(ap.parse_args())

# initialize the video stream and allow the camera sensor to warmup
print("[INFO] starting up camera...")
vs = VideoStream().start()
time.sleep(0)

# start the app
pba = FaceAnalyzerGUI(vs, args["output"])
pba.root.mainloop()