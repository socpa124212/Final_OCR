# ocr.py
from omegaconf import OmegaConf
from ocr_api import ocr_api
import openai
import tiktoken
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
    
    def gpt_API(
        self,
        ocr_script: str,
        ) -> str:

        openai.api_key = self.config.gpt_params.api_key
        tokens_number = self.count_tokens(ocr_script)
        engine = self.config.gpt_params.engine  # 사용할 엔진을 선택합니다.
        prompt = self.config.gpt_prompt.prompt
        max_tokens = self.config.gpt_params.max_tokens

        if tokens_number >= max_tokens:
            prompt_data = ', '.join(ocr_script)

            # Splitting the prompt into chunks based on max_tokens
            prompt_chunks = []
            current_chunk = ""
            for data in prompt_data:
                if self.count_tokens(current_chunk) + self.count_tokens(data) <= max_tokens:
                    current_chunk += ", " + data
                else:
                    prompt_chunks.append(current_chunk)
                    current_chunk = data
            prompt_chunks.append(current_chunk)
            corrected_results = []

            for chunk in prompt_chunks:

                response = openai.Completion.create(
                    engine=engine,
                    prompt=chunk + prompt,
                    max_tokens=max_tokens
                )
                text = response.choices[0].text.strip()
                corrected_results.append(text)
                time.sleep(0.01)
            # Combining the corrected results
            text = " ".join(corrected_results)

        else:
            prompt_data = ', '.join(ocr_script)
            response = openai.Completion.create(
                engine=engine,
                prompt=prompt_data + prompt,
                max_tokens=max_tokens
            )
            text = response.choices[0].text.strip()

        return text

    def count_tokens(self, script):
        engine = self.config.gpt_params.engine
        encoding = tiktoken.encoding_for_model(engine)
        tokens_integer = encoding.encode(str(script))
        return len(tokens_integer)

    def File_gen(self) -> None:
        img_dir = self.config.path.img_pth

        file_list = os.listdir(img_dir)
        file_path_list = [os.path.join(img_dir, file) for file in file_list]

        for path in file_path_list:
            start = time.time() # 이미지 처리 시작시간 기록
            script = self.ocr_tool(img_pth=path)
            tokens = self.count_tokens(script)  # 읽어들인 텍스트의 분량
            result = self.gpt_API(ocr_script=script)
            end = time.time() # 이미지 처리 종료시간 기록:wq

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
                file.write(f"lenth: {tokens}\nstart : {S_time}\nend : {E_time}\nduration : {execution:.2f}")