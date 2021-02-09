import threading
from typing import List

import cv2
from imutils.video import WebcamVideoStream

from image_process import ImageProcess


class VideoFeed:
    def __init__(self, video_stream: WebcamVideoStream,
                 processors: List[ImageProcess] = None):
        if processors is None:
            processors = []
        self.processors = processors
        self.thread_lock = threading.Lock()
        self.video_stream = video_stream
        self.output_frame = None

    def generate(self):
        while True:
            with self.thread_lock:
                if self.output_frame is None:
                    continue
                flag, encoded_image = cv2.imencode(".jpg", self.output_frame)
                if not flag:
                    continue
            yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' +
                   bytearray(encoded_image) + b'\r\n')

    def process(self):
        while True:
            frame = self.video_stream.read()

            for processor in self.processors:
                processor.process(frame)

            with self.thread_lock:
                self.output_frame = frame.copy()

    def stop(self):
        self.video_stream.stop()
