from datetime import datetime

import cv2

from image_process import ImageProcess


class Timestamp(ImageProcess):
    def process(self, frame):
        timestamp = datetime.now()
        cv2.putText(frame, timestamp.strftime(
            "%A %d %B %Y %I:%M:%S%p"), (10, frame.shape[0] - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

