# Emotion Recognition

This project is an emotion recognition application that analyzes images containing faces and detects the emotions expressed by the individuals in those images. It utilizes machine learning techniques and computer vision algorithms to identify and classify emotions.

## Prerequisites 
Before running the app, ensure that you have the following prerequisite:

Python 3.11: The app requires Python 3.11 or a compatible version to run properly. Make sure you have Python 3.11 installed on your system.
If you don't have Python 3.11 installed, you can download and install it from the official Python website (https://www.python.org). Follow the installation instructions specific to your operating system.

You can verify your Python version by opening a terminal or command prompt and running the following command:
```shell
python3 --version

## Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/ruslanliska/face_recognition.git
2. Navigate to the project directory:
   ```shell
   cd face_recognition
   ```
3. Create a virtual environment:
   ```shell 
   python -m venv venv
   ```
4. Activate the virtual environment:

* For Windows:

   ```shell
   . venv\Scripts\activate
   ```
* For macOS/Linux:
   ```shell
   . venv/bin/activate
   ```
4. Install the project dependencies:
   ```shell
   pip install -r requirements.txt
   ```

# Usage
## FastAPI docs
1. Run server:
   ```shell
    uvicorn main:app --reload 
   ```
   You will see:
   ```
   INFO:     Will watch for changes in these directories: ['/path']
   INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
   INFO:     Started reloader process [32614] using StatReload
   ```
2. Go to the URL from (INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)). Usually URL is the same, but it may variate depening on free ports.
3. Go to the provided URL and add /docs to the path, like **http://127.0.0.1:8000/docs**
4. You will see all possible requests, click on desired path and you will see all documentation and you will be able to try it out. Click "Try it out"
5. Provide all required data and click "Execute"
6. See the result in Response Body
### Note
There may be some troubles with running instruction above in Chrome browser, in case you experience some, just change browser. For example, problem with uploading file to form.

## Sending requests to server
1. Run server:
   ```shell
    uvicorn main:app --reload 
   ```
   You will see:
   ```
   INFO:     Will watch for changes in these directories: ['/path']
   INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
   INFO:     Started reloader process [32614] using StatReload
   ```
2. Go to the URL from (INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)). Usually URL is the same, but it may variate depening on free ports.
3. Create request to the server (We provided test requests in test_server_requests.py, you can just run this file with ```python3 test_server_requests.py```
4. Request example:
   ```python
   import requests

   localhost_url = "YOUR LOCALHOST URL"


   image_path = 'PATH_TO_IMAGE'
   # this is the request to detect all emotions on the image provided
   image_detect_url = f'{localhost_url}/image/detect'
   with open(image_path, 'rb') as image:
       files = {'media': image}
       print(requests.post(image_detect_url, files={"file": image}).json())
   ```
