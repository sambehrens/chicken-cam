import threading
import time

from flask import Flask, render_template, Response
from imutils.video import VideoStream

from timestamp import Timestamp
from video_feed import VideoFeed

app = Flask(__name__)

video = VideoFeed(VideoStream(src=0).start(), processors=[Timestamp()])
time.sleep(2.0)


@app.route('/')
def index():
    return render_template('index.html')


@app.route("/video_feed")
def video_feed():
    return Response(video.generate(),
                    mimetype="multipart/x-mixed-replace; boundary=frame")


if __name__ == '__main__':
    t = threading.Thread(target=video.process)
    t.daemon = True
    t.start()

    app.run(host='0.0.0.0', port=5000, debug=True,
            threaded=True, use_reloader=False)

video.stop()
