# 테라폼 S3 버킷 생성 스크립트

# AWS 프로바이더 설정
provider "aws" {
  region = "ap-northeast-2"  # 원하는 AWS 지역으로 변경 가능
}

# S3 버킷 리소스 정의
resource "aws_s3_bucket" "example" {
  bucket = "capston-test"  # 버킷 이름 설정
  force_destroy = true

  # 버킷 태그 설정 (선택 사항)
  tags = {
    Name        = "Example Bucket"
    Environment = "TEST"
  }
}

resource "aws_s3_bucket_ownership_controls" "example" {
  bucket = aws_s3_bucket.example.id
  rule {
    object_ownership = "BucketOwnerPreferred"
  }
}

resource "aws_s3_bucket_public_access_block" "example" {
  bucket = aws_s3_bucket.example.id

  block_public_acls       = false
  block_public_policy     = false
  ignore_public_acls      = false
  restrict_public_buckets = false
}

resource "aws_s3_bucket_acl" "example" {
  depends_on = [
    aws_s3_bucket_ownership_controls.example,
    aws_s3_bucket_public_access_block.example,
  ]

  bucket = aws_s3_bucket.example.id
  acl    = "private"
}
# 실행 및 결과 출력
output "bucket_name" {
  value = aws_s3_bucket.example.id
}
