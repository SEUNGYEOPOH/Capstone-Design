from django.conf import settings
from django.shortcuts import render
from .models import S3Image
from django.core.paginator import Paginator  
import boto3
from imutils.video import VideoStream
import imutils
import cv2,os,urllib.request
import numpy as np
import pandas as pd
import time
from django.http import StreamingHttpResponse
from django.http import HttpResponse
from PIL import Image
import torch
import yolov5
import datetime
import boto3,botocore
import threading
import signal


# Create your views here.
def index(request):
    page = request.GET.get('page', '1')  # 페이지
    #time_now = tt()
    #context = {'dbdb_list': db_list}
    return render(request,'index.html')
def dbdb(request):
    db_list = S3Image.objects.order_by('-id')
    context = {'dbdb_list': db_list}
    return render(request, 'dbdb_list.html', context)

def tt():
    #while True:
    current_time = time.strftime('%Y-%m-%d %I:%M:%S %p', time.localtime(time.time()))
    return current_time
     # 1초마다 업데이트됨

def time_feed(request):
    current_time = time.strftime('%Y-%m-%d %I:%M:%S %p', time.localtime(time.time()))
    context = {'time_now': current_time}
    return render(request, 'time_feed.html', context)


#def time_feed(request):
#    return HttpResponse(tt())

### S3 bucket 클라이언트 객체 생성 ###
s3_bucket_name = 'capston-test'  # 저장할 S3 버킷 이름
s3_client = boto3.client('s3')
############
cfg_model_path = 'models/yolov5s.pt'
model = None
confidence = .25
if torch.cuda.is_available():
    device = 'cuda'
else:
    device = 'cpu'
##

def load_model(path, device):
    model_ = yolov5.load('models/yolov5s.pt')
    model_.to(device)
    print("model to ", device)
    return model_


model = load_model(cfg_model_path, device)


def infer_image(img,confidence, size=None):
    model.conf = confidence
    result = model(img, size=size) if size else model(img)
    result.render()
    image = result.ims[0]
    return image

###############

class VideoStreamThread(threading.Thread):
    def __init__(self,url):
        super().__init__()
        self.frame = None
        self.stop_event = threading.Event()
        self.lock = threading.Lock()
        self.url = url

    def run(self):
        if self.url == 'webcam':
            cap = cv2.VideoCapture(0)
        else:
            cap = cv2.VideoCapture(self.url)
        ##
        fps = cap.get(cv2.CAP_PROP_FPS) 
        wt = 1 / fps
        ##
        confidence = 0.45
        model.classes = [0]
        while not self.stop_event.is_set():
            ## 프레임 보정을 위한 start_time과 매분 1장의 사진을 찍기위한 현재시각 저장용 today 변수 생성
            start_time = time.time()
            today = datetime.datetime.today()
            ##
            ret, frame = cap.read()
            if not ret:
                print("Error: failed to capture image")
                continue
            # 객체탐지 수행
            results = infer_image(frame,confidence)
            
            #results = np.array(results) # 불필요한 작업이라 생략
            # 면적 넣는 부분
            cv2.putText(results, f'AREA:', (30,30), cv2.FONT_HERSHEY_PLAIN, 2,
                        (0,0,255), 2, cv2.LINE_AA)
            
            # 일단 5초마다 s3에 사진 넣고 db에 insert하기
            if (today.second % 10 == 0) and (today.microsecond > 0 and today.microsecond < 100000) :
                    # 현재 시간을 파일 이름으로 사용
                current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                current_time_db = datetime.datetime.now().isoformat()
                image_file_name = f"{current_time}.jpg"

                # 이미지 파일 저장
                cv2.imwrite(f"screenshot/{image_file_name}", results)

                try:
                    # S3로 이미지 업로드 public-read임.
                    s3_client.upload_file(f"./screenshot/{image_file_name}", s3_bucket_name, f"screenshot/{image_file_name}",ExtraArgs={'ACL': 'public-read'})
                    print(f"이미지가 성공적으로 S3 버킷 '{s3_bucket_name}'에 업로드되었습니다.")
                    image_url = f"https://{s3_bucket_name}.s3.amazonaws.com/screenshot/{image_file_name}"
                    q = S3Image(c_date=current_time_db, img_url=image_url)
                    q.save()
                except botocore.exceptions.ClientError as e:
                    print(f"S3 업로드 에러: {e.response['Error']['Code']}")

            results = cv2.imencode('.jpg', results)[1].tobytes()
            ##
            dt = time.time() - start_time
            if wt - dt > 0:
                time.sleep(wt - dt)
            ##
            with self.lock:
                self.frame = results

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

# 백그라운드에서 탐지 시작
video_thread = VideoStreamThread('webcam')
video_thread.start()


def video_feed(request):
    def generate():
        while True:
            frame = video_thread.get_frame()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

    return StreamingHttpResponse(generate(), content_type='multipart/x-mixed-replace; boundary=frame')