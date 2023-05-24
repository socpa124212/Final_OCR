From python:3.8

# 작업 디렉토리를 설정
WORKDIR /app

RUN python -m pip install --upgrade pip
# 의존성 파일을 Docker 이미지로 복사
COPY requirements.txt .
# EasyOCR의 Python 패키지
RUN pip install --no-cache-dir -r requirements.txt
# open-cv de[emdecy file update
RUN apt-get update && apt-get -y install libgl1-mesa-glx
