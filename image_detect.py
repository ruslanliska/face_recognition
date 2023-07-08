from detection_utils.utils import open_image_cv

from fer import FER
import cv2

from const import AVALIABLE_EMOTIONS

emotion_detector = FER(mtcnn=True)


def detect_emotions(image_path: str) -> dict[str, str | list[dict[str, list | dict]]] | None:
    """
    Detects emotions in the given image and returns the results.

    Args:
        image_path (str): Path to the image file.

    Returns:
        Union[dict[str, str | list[dict[str, list | dict]]], None]: A dictionary containing the detected emotions
            and related information. The dictionary structure is as follows:
                - 'top_emotion' (str): The top emotion detected in the image.
                - 'top_emotion_score' (str): The score or confidence level of the top emotion.
                - 'all_emotions' (list[dict[str, list | dict]]): A list of dictionaries containing information
                    about each detected emotion. Each dictionary contains the following keys:
                    - 'box' (list): The bounding box coordinates of the detected face.
                    - 'emotions' (dict): A dictionary of emotions and their corresponding scores.

            If no emotions are detected, None is returned.
    """
    # Image processing code to detect emotions and visualize results
    image = open_image_cv(image_path)
    emotions = emotion_detector.detect_emotions(image)
    top_emotion, top_emotion_score = emotion_detector.top_emotion(image)
    for i in emotions:
        bounding_box = i["box"]
        cv2.rectangle(image,
                      (bounding_box[0], bounding_box[1]),
                      (bounding_box[0] + bounding_box[2], bounding_box[1] + bounding_box[3]),
                      (36, 255, 12), 2, )

        cv2.putText(image, max(i['emotions'], key=i['emotions'].get), (bounding_box[0], bounding_box[1] - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (36, 255, 12), 2)

    cv2.imwrite(image_path, image)

    # Return the result dictionary if emotions are detected, otherwise return None
    if emotions:
        result_dict = {
            'top_emotion': top_emotion,
            'top_emotion_score': top_emotion_score,
            'all_emotions': emotions
        }
        return result_dict
    return None


def detect_specific_emotion(image_path: str, emotion: str) -> dict[str, str | list[dict[str, list | dict]]]:
    """
    Detects a specific emotion in the given image and returns the result.

    Args:
        image_path (str): Path to the image file.
        emotion (str): The specific emotion to detect.

    Returns:
        dict[str, str | list[dict[str, list | dict]]]: A dictionary containing the result of detecting the specific
        emotion in the image. The dictionary structure is as follows:

            If the desired emotion is found:
                - 'Emotion' (str): The name of the detected emotion.
                - 'Emotion Score' (str): The score or confidence level of the detected emotion.

            If the desired emotion is not available among the detected emotions:
                - 'message' (str): A message indicating that the desired emotion is not available.
                - 'found_emotions' (list[dict[str, list | dict]]): A list of dictionaries containing information
                    about each detected emotion. Each dictionary contains the following keys:
                    - 'box' (list): The bounding box coordinates of the detected face.
                    - 'emotions' (dict): A dictionary of emotions and their corresponding scores.

            If no emotions are detected:
                - 'message' (str): A message indicating that no emotions were found in the image.

            If multiple emotions are detected:
                - 'message' (str): A message indicating that multiple emotions were found in the image. The user is
                    instructed to upload an image with only one face.
                - 'found_emotions' (list[dict[str, list | dict]]): A list of dictionaries containing information
                    about each detected emotion. Each dictionary contains the following keys:
                    - 'box' (list): The bounding box coordinates of the detected face.
                    - 'emotions' (dict): A dictionary of emotions and their corresponding scores.

    """
    emotions = detect_emotions(image_path)

    if emotion not in AVALIABLE_EMOTIONS and emotions:
        return {'message': 'Desired emotion is not avaliable!',
                'found_emotions': emotions}

    if not emotions:
        return {'message': 'No emotions found on image!'}

    if len(emotions.get('all_emotions')) > 1:
        return {'message': 'Multiple emotions found on image. Please, upload only one face.',
                'found_emotion': emotions}

    all_emotions = emotions.get('all_emotions')

    emotion_score = all_emotions[0]['emotions'].get(emotion)
    return {'Emotion': emotion,
            'Emotion Score': emotion_score}
