import hydra
from ocr import OCR
import os
import time

@hydra.main(version_base=None, config_path="./", config_name="config")
def run_ocr(config) -> None:
    ocr_instance = OCR(config = config) # config 호출?
    img_dir = config.path.img_pth
    file_list = os.listdir(img_dir)
    file_path_list = [os.path.join(img_dir, file) for file in file_list]

    for path in file_path_list:
        start = time.time() # 이미지 처리 시작시간 기록
        script = ocr_instance.ocr_api(img_pth=path)
        result = ocr_instance.gpt_API(ocr_script=script, config=config)
        end = time.time() # 이미지 처리 종료시간 기록
        execution = end - start 
        file_name = os.path.basename(path)
        output = config.path.text_pth + file_name + config.path.output_ext

        with open(output, "w") as file: # file output write
            file.write("ocr result" + config.ocr.api + "\n")
            file.write(''.join(script) + "\n\n")
            file.write("gpt parsing+correction \n")
            file.write(result + "\n\n")
            file.write(f"start : {start}\nend : {end}\nduration : {execution}")

# run_ocr()

if __name__ == "__main__":
    run_ocr()