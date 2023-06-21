import os

os.environ["IMAGEIO_FFMPEG_EXE"] = "/usr/bin/ffmpeg"

from fer import FER
import cv2

from utils import open_image_cv

emotion_detector = FER(mtcnn=True)


def detect_emotions(image_path: str):
    image = open_image_cv(image_path)
    emotions = emotion_detector.detect_emotions(image)
    print(emotions)
    top_emotion, top_emotion_score = emotion_detector.top_emotion(image)
    print(top_emotion, top_emotion_score)
    # bounding_box = emotions[0]["box"]
    for i in emotions:
        bounding_box = i["box"]
        cv2.rectangle(image,
                      (bounding_box[0], bounding_box[1]),
                      (bounding_box[0] + bounding_box[2], bounding_box[1] + bounding_box[3]),
                      (36, 255, 12), 2, )
        cv2.putText(image, max(i['emotions'], key=i['emotions'].get), (bounding_box[0], bounding_box[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (36, 255, 12), 2)

    cv2.imshow('with emotions', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return emotions


detect_emotions('test_static/test_group3.png')
