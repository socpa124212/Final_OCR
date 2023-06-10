# ocr_util.py
from PIL import Image
from pororo import Pororo
import easyocr
from pytesseract import *
from paddleocr import PaddleOCR,draw_ocr

def pororo(img_pth: str) -> str:
    ocr = Pororo(task="ocr", lang="ko")
    result = ocr(img_pth)
    return result


def EasyOCR(img_pth: str) -> str:
    reader = easyocr.Reader(['ko', 'en'], gpu=False)
    result = reader.readtext(img_pth)
    txt = [line[1] for line in result]
    return txt


def tesseract(img_pth: str) -> str:
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image, lang='kor')  # 한글 언어 설정
    result = text.replace('\r', '')
    return result


def paddleocr(img_pth: str) -> str :
    ocr = PaddleOCR(use_angle_cls=True, lang='korean')
    result = ocr.ocr(img_pth, cls=True)
    # result :좌표, 결과, 정확도
    result = result[0]
    txts = [line[1][0] for line in result]
    return txts