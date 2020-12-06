import cv2
import queue
import threading


class read_cam(threading.Thread):
    def __init__(self, src = 0 , *args, **kwargs):
        threading.Thread.__init__(self, *args, **kwargs)
        self.cap = cv2.VideoCapture(src)
        self.width = int(self.cap.get(3))
        self.height = int(self.cap.get(4))
        self.event = threading.Event()
        self.queue =queue.Queue()
        self.face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    def run(self):
        self.event.wait()
        while (self.event.isSet()):
            _, frame = self.cap.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = self.face_cascade.detectMultiScale(gray, 1.3, 5)
            for (x,y,w,h) in faces:
                cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,225),2)
            self.queue.put(frame)
            cv2.waitKey(1)
        self.run()