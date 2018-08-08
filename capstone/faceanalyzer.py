import cv2
import os
import tkinter as tk
from PIL import Image
from PIL import ImageTk
import threading
import imutils


class FaceAnalyzerGUI:
    def __init__(self, video, output_path):
        self.video = video
        self.output_path = output_path
        self.frame = None
        self.thread = None
        self.stop_event = None

        self.root = tk.Tk()
        self.root.lift()
        self.root.attributes("-topmost", True)
        self.panel = None

        button = tk.Button(self.root, text="Capture", command=self.take_picture)
        button.pack(side="bottom", fill="both", expand="yes", padx=10, pady=10)

        # thread to pool video stream for most recent frame
        self.stop_event = threading.Event()
        self.thread = threading.Thread(target=self.video_loop, args=())
        self.thread.start()

        # callback to handle window closing
        self.root.wm_title("FrameFind")
        self.root.wm_protocol("WM_DELETE_WINDOW", self.on_close)

    def video_loop(self):
        try:
            while not self.stop_event.is_set():
                self.frame = self.video.read()
                self.frame = imutils.resize(self.frame, width=720)

                image = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
                image = Image.fromarray(image)
                image = ImageTk.PhotoImage(image)

                if self.panel is None:
                    self.panel = tk.Label(image=image)
                    self.panel.image = image
                    self.panel.pack(side="left", padx=10, pady=10)
                else:
                    self.panel.configure(image=image)
                    self.panel.image = image
        except RuntimeError:
            print("[INFO] RuntimeError")

    def take_picture(self):
        # creates output path
        path = os.path.sep.join((self.output_path, "face.jpg"))

        # saves picture
        cv2.imwrite(path, self.frame.copy())
        print("[INFO] Saved")
        self.stop_event.set()
        self.video.stop()

    def print_result(self, result):
        print()

    def on_close(self):
        print("[INFO] Closing program")
        self.stop_event.set()
        self.video.stop()
        self.root.quit()

