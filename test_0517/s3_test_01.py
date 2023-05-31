import boto3
import os

s3_bucket_name = 'capston-test'  # 저장할 S3 버킷 이름
s3_client = boto3.client('s3')

current_directory = os.getcwd()  # 현재 작업 디렉토리 경로

file_names = os.listdir(current_directory)  # 현재 디렉토리의 파일 및 디렉토리 목록 조회

# .jpg로 끝나는 파일 S3 버킷에 저장
for file_name in file_names:
    if file_name.endswith(".jpg") and os.path.isfile(file_name):  # .jpg로 끝나는 파일 중 파일인 경우에만 처리
        s3_object_key = file_name  # S3 객체 키는 파일명으로 설정

        # S3 버킷에 파일 업로드
        s3_client.upload_file(file_name, s3_bucket_name, s3_object_key, ExtraArgs={'ACL': 'public-read'})
        image_url = f"https://{s3_bucket_name}.s3.amazonaws.com/{s3_object_key}"

        print(f"Uploaded {file_name} to S3 bucket: {s3_bucket_name}")
        print("Image URL:", image_url)
        print('=========================================================')
