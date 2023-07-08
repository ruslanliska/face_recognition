import uuid

from fastapi import FastAPI, File, UploadFile

from const import STATIC_IMAGES_PATH
from image_detect import (detect_emotions,
                          detect_specific_emotion)

app = FastAPI(title='Emotion detection',
              description='App for emotion detection on the face',
              version="0.1.0")


@app.get('/')
def index() -> dict[str, str]:
    return {'Connection': 'Success'}


@app.post('/image/detect')
async def image_detect_emotions(file: UploadFile = File(...)) -> dict[str, str | list[dict[str, list | dict]]]:
    """
    Detects emotions in the uploaded image and returns the result.

    Args:
        file (UploadFile): The uploaded image file.

    Returns:
        dict[str, str | list[dict[str, list | dict]]]: A dictionary containing the result of detecting emotions
            in the image. The dictionary structure is as follows:
            - If emotions are detected:
                - 'top_emotion' (str): The top emotion detected in the image.
                - 'top_emotion_score' (str): The score or confidence level of the top emotion.
                - 'all_emotions' (list[dict[str, list | dict]]): A list of dictionaries containing information
                    about each detected emotion. Each dictionary contains the following keys:
                    - 'box' (list): The bounding box coordinates of the detected face.
                    - 'emotions' (dict): A dictionary of emotions and their corresponding scores.
            - If no people are detected in the image:
                - 'message' (str): A message indicating that there are no people in the photo.
    """
    contents = await file.read()
    file.filename = f"{uuid.uuid4()}.png"
    file_dir = f'{STATIC_IMAGES_PATH}{file.filename}'

    with open(file_dir, 'wb') as f:
        f.write(contents)

    emotions = detect_emotions(file_dir)
    if emotions:
        return emotions
    return {'message': 'There is no people on the photo'}


@app.post('/image/detect/{emotion}')
async def image_detect_specific_emotion(emotion: str, file: UploadFile = File(...)):
    """
    Detects a specific emotion in the uploaded image and returns the result.

    Args:
        emotion (str): The specific emotion to detect.
        file (UploadFile): The uploaded image file.

    Returns:
        dict[str, str | list[dict[str, list | dict]]]: A dictionary containing the result of detecting the specific
        emotion in the image. The dictionary structure is as follows:
        - If the desired emotion is found:
            - 'Emotion' (str): The name of the detected emotion.
            - 'Emotion Score' (str): The score or confidence level of the detected emotion.
        - If the desired emotion is not available among the detected emotions:
            - 'message' (str): A message indicating that the desired emotion is not available.
            - 'found_emotions' (list[dict[str, list | dict]]): A list of dictionaries containing information
                about each detected emotion. Each dictionary contains the following keys:
                - 'box' (list): The bounding box coordinates of the detected face.
                - 'emotions' (dict): A dictionary of emotions and their corresponding scores.
        - If no emotions are detected:
            - 'message' (str): A message indicating that no emotions were found in the image.
        - If multiple emotions are detected:
            - 'message' (str): A message indicating that multiple emotions were found in the image.
              The user is instructed to upload an image with only one face.
    """
    contents = await file.read()
    file.filename = f"{uuid.uuid4()}.png"
    file_dir = f'{STATIC_IMAGES_PATH}{file.filename}'

    with open(file_dir, 'wb') as f:
        f.write(contents)
    return detect_specific_emotion(image_path=file_dir,
                                   emotion=emotion)
