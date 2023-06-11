import hydra
from ocr import OCR
import os
import time

@hydra.main(version_base=None, config_path="./", config_name="config")
def run_ocr(config) -> None:
    ocr_instance = OCR(config = config) # config 호출
    ocr_instance.File_gen()

run_ocr()

# if __name__ == "__main__":
#     run_ocr()