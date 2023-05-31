# paddlepaddle & paddleocr 설치
# pip install paddlepaddle -i https://pypi.tuna.tsinghua.edu.cn/simple
# pip install "paddleocr>=2.0.1"
from paddleocr import PaddleOCR,draw_ocr
ocr = PaddleOCR(use_angle_cls=True, lang='korean')
img_path = './image1.PNG'
result = ocr.ocr(img_path, cls=True)

# result :좌표, 결과, 정확도
result = result[0]
txts = [line[1][0] for line in result]
print(txts)
