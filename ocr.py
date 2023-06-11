# ocr.py
from omegaconf import OmegaConf
from ocr_api import ocr_api
import openai
import os, time
from datetime import datetime

class OCR:
    def __init__(
        self,
        config: OmegaConf
        ) -> None:

        self.config = config
        self.ocr_api = ocr_api(config)

        if config.ocr.api == "pororo":
            self.ocr_tool = self.ocr_api.pororo
        elif config.ocr.api == "easy":
            self.ocr_tool = self.ocr_api.EasyOCR
        elif config.ocr.api == "paddle":
            self.ocr_tool = self.ocr_api.paddleocr
        elif config.ocr.api == "tesseract":
            self.ocr_tool = self.ocr_api.tesseract
    
    def gpt_API(self,
        ocr_script: str,
        ) -> str:

        openai.api_key = self.config.gpt_params.api_key
        script = ', '.join(ocr_script)
        response = openai.Completion.create(
                    engine = self.config.gpt_params.engine,  # 사용할 엔진을 선택합니다.
                    prompt = script + self.config.gpt_prompt.prompt,
                    max_tokens = self.config.gpt_params.max_tokens  # 모델이 생성할 최대 토큰 수를 지정합니다.
                    )

        text = response.choices[0].text
        return text
    
    def File_gen(self) -> None:
        img_dir = self.config.path.img_pth

        file_list = os.listdir(img_dir)
        file_path_list = [os.path.join(img_dir, file) for file in file_list]

        for path in file_path_list:
            start = time.time() # 이미지 처리 시작시간 기록
            script = self.ocr_tool(img_pth=path)
            result = self.gpt_API(ocr_script=script)
            end = time.time() # 이미지 처리 종료시간 기록
            execution = end - start 
            file_name = os.path.basename(path)
            output = self.config.path.text_pth + file_name + self.config.path.output_ext

            S_time = str(datetime.utcfromtimestamp(start).strftime('%H:%M:%S')) # UTC 기준으로 표시되는 시간표기
            E_time = str(datetime.utcfromtimestamp(end).strftime('%H:%M:%S')) 

            with open(output, "w") as file: # file output write
                file.write("<ocr result " + self.config.ocr.api + ">\n")
                file.write(''.join(script) + "\n\n")
                file.write("<gpt parsing+correction>")
                file.write(result + "\n\n")
                file.write(f"start : {S_time}\nend : {E_time}\nduration : {execution:.2f}")