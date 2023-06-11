# ocr_util.py
from PIL import Image
from pororo import Pororo
import easyocr
from pytesseract import pytesseract
from paddleocr import PaddleOCR,draw_ocr
from omegaconf import OmegaConf

class ocr_api :
    def __init__(
        self,
        config: OmegaConf
        ) -> None:

        self.config = config


    def pororo(
        self, 
        img_pth: str
        ) -> str:

        ocr = Pororo(task="ocr", lang=self.config.ocr.pororo.lang)
        result = ocr(img_pth)

        return result


    def EasyOCR(
        self, 
        img_pth: str
        ) -> str:

        reader = easyocr.Reader(self.config.ocr.easy.lang, gpu=self.config.ocr.easy.GPU)
        result = reader.readtext(img_pth)
        # easyocr.Reader.readtext() returns list of tuple about detection
        # form : ([coordination], result, accuracy)
        txt = [line[1] for line in result]

        return txt


    def tesseract(
        self, 
        img_pth: str
        ) -> str:

        image = Image.open(img_pth)
        text = pytesseract.image_to_string(image, lang=self.config.ocr.tesseract.lang)
        result = text.replace('\r', '')

        return result


    def paddleocr(
        self, 
        img_pth: str
        ) -> str :

        ocr = PaddleOCR(use_angle_cls=True, lang=self.config.ocr.paddle.lang)
        result = ocr.ocr(img_pth, cls=True)
        # PaddleOCR.ocr() returns str that indicate detected text as list(size=1) 
        # form : [[coordination], (result, accuracy)]    
        result = result[0] # result element extraction
        txts = [line[1][0] for line in result] # text extraction

        return txts