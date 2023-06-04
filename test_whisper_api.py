import os
import requests


def whisper_api(folder_path, file_path):
    
    OPENAI_API_KEY = os.environ['OPENAI_API_KEY']

    url = 'https://api.openai.com/v1/audio/transcriptions'
    headers = {'Authorization': f'Bearer {OPENAI_API_KEY}'}
    files = {'file': open(file_path, 'rb'),
            'model': (None, 'whisper-1')
    }
    response = requests.post(url, headers=headers, files=files)
    output_path = os.path.join(folder_path, os.path.splitext(os.path.basename(file_path))[0] + '.' + 'txt')
    with open(output_path, 'w') as f:
        f.write(response.content.decode('utf-8'))

whisper_api()
