# Easy OCR                                                             

[Easy OCR github](https://github.com/JaidedAI/EasyOCR)

Easy OCR is a simple and efficient optical character recognition (OCR) tool that allows you to extract text from images. With Easy OCR, you can easily process images containing text and obtain the corresponding textual information.


## Requirements

torch

easyocr

opencv-python


## Installation

To install Easy OCR, follow these steps:

1.Clone the repository:

`git clone https://github.com/socpa124212/Final_OCR.git`

2. Navigate to the project directory:

`cd Final_OCR/easy_ocr_test`

3. Install the module using pip:

`pip install easyocr`


## Usage
```
import easyocr

reader = easyocr.Reader(['ko', 'en'], gpu=False)
result = reader.readtext('sample_label.png')
print(result)
```
