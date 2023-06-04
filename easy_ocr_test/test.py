import easyocr

reader = easyocr.Reader(['ko', 'en'], gpu=False)
result = reader.readtext('sample_label.png')
print(result)