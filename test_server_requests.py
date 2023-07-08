import requests

localhost_url = "http://127.0.0.1:8000"


image_path = 'test_static/test_happy_woman.png'

# DETECT ALL EMOTIONS FOUND ON IMAGE
image_detect_url = f'{localhost_url}/image/detect'
with open(image_path, 'rb') as image:
    files = {'media': image}
    print(requests.post(image_detect_url, files={"file": image}).json())


#DETECT SCORE OF PROVIDED EMOTION
desired_emotion = 'happy'
image_detect_emotion = f'{localhost_url}/image/detect/{desired_emotion}'
with open(image_path, 'rb') as image:
    files = {'media': image}
    print(requests.post(image_detect_emotion, files={"file": image}).json())

