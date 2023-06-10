# ocr.py
from omegaconf import OmegaConf
from ocr_api import *
import openai

class OCR:
    def __init__(
        self,
        config: OmegaConf
        ) -> None:

        self.config = config

        if config.ocr.api == "pororo":
            self.ocr_api = pororo
        elif config.ocr.api == "easy":
            self.ocr_api = EasyOCR
        elif config.ocr.api == "paddle":
            self.ocr_api = paddleocr
        elif config.ocr.api == "tesseract":
            self.ocr_api = tesseract
    
    def gpt_API(self,
        ocr_script: str,
        config: OmegaConf
        ) -> str:
        openai.api_key = config.gpt_params.api_key
        script = ', '.join(ocr_script)
        response = openai.Completion.create(
                    engine = config.gpt_params.engine,  # 사용할 엔진을 선택합니다.
                    prompt = script + config.gpt_prompt.prompt,
                    max_tokens = config.gpt_params.max_tokens  # 모델이 생성할 최대 토큰 수를 지정합니다.
                    )

        text = response.choices[0].text
        return text