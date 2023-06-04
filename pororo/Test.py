from pororo import Pororo
import openai
import os

def get_files_without_full(directory):
    file_list = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if "full" not in file:
                file_list.append(os.path.join(root, file))
    return file_list

# 예시: "my_directory" 디렉토리에서 "full" 단어가 포함되지 않은 파일 목록 가져오기
directory = "./assets/image_data"
files = get_files_without_full(directory)
openai.api_key = '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'

#IMAGE_PATH = "/app/assets/image_data/27.png"
ocr = Pororo(task="ocr", lang="ko")
for path in files:
    result = ocr(path)

    prompt_data = ', '.join(result)
    prompt = prompt_data + '''

    Above text data is korean food information label that is not parsed. 
    Also partial correction is needed.
    Parse and correct given text data as possible as you can.
    Most of the word should be related with food.
    text data should be in Korean
    '''

    response = openai.Completion.create(
      engine='text-davinci-003',  # 사용할 엔진을 선택합니다.
      prompt=prompt,
      max_tokens=1500  # 모델이 생성할 최대 토큰 수를 지정합니다.
    )

    text = response.choices[0].text
    output = os.path.basename(path).split(".")[0]
    output_file_path = "/app/assets/ocr_result(ocr+gpt)/" + output +'.txt'

    with open(output_file_path, "w") as file:
        file.write(text)