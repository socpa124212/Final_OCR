# Final_OCR
### 프로젝트 구조
이 프로젝트는 아래와 같은 구조를 가지고 있습니다:

- .gitignore : Git에 업로드하지 않을 파일 및 디렉토리를 지정합니다.
- Dockerfile : Docker 이미지를 빌드하기 위한 명령어가 포함되어 있습니다.
- docker-compose.yml : 여러 Docker 컨테이너를 동시에 관리하고 실행하는데 사용됩니다.
- config.yaml : OCR 및 GPT 설정에 대한 정보를 포함하고 있습니다.
- ocr.py : OCR 작업을 수행하고, 추출된 텍스트를 GPT 모델에 전달하여 분석하고 수정하는 클래스를 정의합니다.
- ocr_api.py : 여러 OCR 엔진들(pororo, easyocr, tesseract, paddleocr)의 클래스를 정의합니다.
- run_ocr.py : OCR 클래스를 생성하고 실행하는 메인 스크립트입니다.
- requirements.txt : 이 프로젝트를 실행하기 위해 필요한 Python 라이브러리를 리스트업해 놓았습니다.

### 사용 방법
#### Docker를 이용한 사용 방법

1. Docker 및 Docker-compose가 설치되어 있는지 확인하십시오.

2. Git Repository를 Clone하십시오.
```
git clone https://github.com/socpa124212/Final_OCR
cd Final_OCR
```

3. Docker 이미지를 빌드하고 실행하십시오.
```
docker-compose build
docker-compose up
```

#### Python 환경에서 직접 실행하는 방법
1. Git Repository를 Clone하십시오.
```
git clone https://github.com/socpa124212/Final_OCR
cd Final_OCR
```

2. 필요한 Python 라이브러리를 설치하십시오.
```
pip install -r requirements.txt
```

3. OCR를 실행하십시오.
```
python run_ocr.py
```

### 주의사항
이 프로젝트는 GPT 모델의 API 키를 사용하므로, 이를 config.yaml에서 적절하게 설정해주어야 합니다.

또한, OCR을 수행할 이미지 파일 및 GPT의 결과를 저장할 디렉토리를 config.yaml에서 설정해주어야 합니다.
