FROM python:3.8

# 패키지 설치를 위해서 터미널을 interactive하지 않게 변경
ENV DEBIAN_FRONTEND=noninteractive

# 작업 디렉토리를 설정
WORKDIR /app

RUN python -m pip install --upgrade pip
# 의존성 파일을 Docker 이미지로 복사
COPY requirements.txt .
# 필요한 파이썬 패키지와 필요한 
RUN pip install --no-cache-dir -r requirements.txt
# open-cv dependecy file update
# tesseract-ocr 설치
# libtesseract4 설치가 되지 않는 상태가 있음
RUN apt-get update && apt-get -y install libgl1-mesa-glx
RUN apt-get update && apt-get -y install tesseract-ocr tesseract-ocr-kor