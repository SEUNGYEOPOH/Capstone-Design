from django.shortcuts import render
from django.http import StreamingHttpResponse
import yolov5,torch
from yolov5.utils.general import *
from yolov5.utils.torch_utils import select_device, time_sync
from yolov5.utils.plots import Annotator, colors
from deep_sort.utils.parser import get_config
from deep_sort.deep_sort import DeepSort
import cv2
from PIL import Image as im
import datetime
import threading
# Create your views here.
def index(request):
    return render(request,'index.html')
print(torch.cuda.is_available())
#load model
model = yolov5.load('yolov5s.pt')
# model = torch.hub.load('ultralytics/yolov5', 'yolov5s')
device = select_device() # 0 for gpu, '' for cpu
# initialize deepsort
cfg = get_config()
cfg.merge_from_file("deep_sort/configs/deep_sort.yaml")
deepsort = DeepSort('osnet_x0_25',
                    device,
                    max_dist=cfg.DEEPSORT.MAX_DIST,
                    max_iou_distance=cfg.DEEPSORT.MAX_IOU_DISTANCE,
                    max_age=cfg.DEEPSORT.MAX_AGE, n_init=cfg.DEEPSORT.N_INIT, nn_budget=cfg.DEEPSORT.NN_BUDGET,
                    )
# Get names and colors
names = model.module.names if hasattr(model, 'module') else model.names

import threading
import signal

class VideoStreamThread(threading.Thread):
    def __init__(self):
        super().__init__()
        self.frame = None
        self.stop_event = threading.Event()
        self.lock = threading.Lock()

    def run(self):
        cap = cv2.VideoCapture(0)
        model.conf = 0.45
        model.iou = 0.5
        model.classes = [0, 64, 39]
        while not self.stop_event.is_set():
            ret, frame = cap.read()
            if not ret:
                print("Error: failed to capture image")
                break

            results = model(frame, augment=True)
            # process
            annotator = Annotator(frame, line_width=2, pil=not ascii)
            det = results.pred[0]
            if det is not None and len(det):
                xywhs = xyxy2xywh(det[:, 0:4])
                confs = det[:, 4]
                clss = det[:, 5]
                outputs = deepsort.update(xywhs.cpu(), confs.cpu(), clss.cpu(), frame)
                if len(outputs) > 0:
                    for j, (output, conf) in enumerate(zip(outputs, confs)):
                        bboxes = output[0:4]
                        
                        id = output[4]
                        cls = output[5]

                        c = int(cls)  # integer class
                        label = f'{id} {names[c]} {conf:.2f}'
                        annotator.box_label(bboxes, label, color=colors(c, True))
                        '''
                        # Check if the object ID is 5 and save the image
                        print(output,type(output))
                        ################
                        if id >= 5:
                            filename = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S.jpg")
                            cv2.imwrite(filename, annotator.result())
                            #id_ = 0
                        #    #output[4] = id_
                        ################
                        '''
            else:
                deepsort.increment_ages()

            with self.lock:
                self.frame = annotator.result()

        cap.release()

    def stop(self):
        self.stop_event.set()

    def get_frame(self):
        with self.lock:
            return self.frame

def signal_handler(sig, frame):
    print('Exiting...')
    video_thread.stop()
    video_thread.join()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

video_thread = VideoStreamThread()
video_thread.start()

def video_feed(request):
    def generate():
        while True:
            frame = video_thread.get_frame()
            image_bytes = cv2.imencode('.jpg', frame)[1].tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + image_bytes + b'\r\n')

    return StreamingHttpResponse(generate(), content_type='multipart/x-mixed-replace; boundary=frame')
