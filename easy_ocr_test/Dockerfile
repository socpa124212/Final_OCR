# 기본 파이썬 이미지 사용
FROM python:3.8

# 작업 디렉토리 설정
WORKDIR /app

RUN python -m pip install --upgrade pip
# 필요한 라이브러리 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
# open-cv dependecy file update
RUN apt-get update && apt-get -y install libgl1-mesa-glx

# 소스 코드 복사
COPY . .

# 컨테이너 실행시 실행될 명령
# CMD ["tail", "-f", "/dev/null"]