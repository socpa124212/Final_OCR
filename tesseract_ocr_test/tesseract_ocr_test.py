import pytesseract
from PIL import Image

# Tesseract OCR의 설치 경로를 지정해줍니다.
pytesseract.pytesseract.tesseract_cmd = "tesseract file path" + "tesseract.exe"
# 대부분의 설치경로 = C:/Program Files/Tesseract-OCR/

# 이미지를 열고 OCR을 실행합니다.
def ocr_image(image_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image, lang='kor')  # 한글 언어 설정
    return text.replace('\r', '')

# 이미지 파일 경로를 지정합니다.
image_path = 'image path'

# 이미지에서 텍스트 추출
extracted_text = ocr_image(image_path)

# 추출된 텍스트 출력
print(extracted_text)

