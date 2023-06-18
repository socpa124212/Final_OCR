English | [한국어](README.md)

# Final_OCR
This project includes code that uses Optical Character Recognition (OCR) to extract text from images and then uses the GPT model to analyze and correct the extracted text.

### Project Structure

The project is structured as follows:

- .gitignore : Specifies files and directories that should not be uploaded to Git.
- Dockerfile : Contains the instructions to build the Docker image.
- docker-compose.yml : Used to manage and run multiple Docker containers at the same time.
- config.yaml : Contains information about the OCR and GPT settings.
- ocr.py : Defines a class that performs OCR tasks, passes the extracted text to the GPT model for analysis and correction.
- ocr_api.py : Defines classes for different OCR engines (pororo, easyocr, tesseract, paddleocr).
- run_ocr.py : The main script that creates and runs the OCR class.
- requirements.txt : Lists the Python libraries required to run this project.

### How to Use
#### Using Docker
1. Ensure Docker and Docker-compose are installed.

2. Clone the Git Repository.
```
git clone https://github.com/socpa124212/Final_OCR.git
cd Final_OCR
```

3. Build and run the Docker image.
```
docker-compose build
docker-compose up
```

#### Running Directly in Python Environment
1. Clone the Git Repository.
```
!git clone https://github.com/socpa124212/Final_OCR.git
cd Final_OCR
```

2. Install the necessary Python libraries.
```
!pip install -r requirements.txt
```

3. Run OCR.
```
!python run_ocr.py
```

### Note
This project uses an API key for the GPT model, which should be properly set in config.yaml.

Also, the directories for the images to perform OCR on and for storing the GPT results should be set in config.yaml.
