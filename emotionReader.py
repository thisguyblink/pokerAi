from deepface import DeepFace
import cv2
from PIL import Image
import numpy as np

def read_image(image):
    img = read_image_as_cv2(image)
    result = DeepFace.analyze(img, actions=['emotion'], enforce_detection=False)

    print(result[0]['emotion'])

    negative = ['contempt', 'anger', 'fear', 'disgust', 'sad']
    positive = ['surprised', 'happy']

    pos = 0
    neg = 0
    for k, v in result[0]['emotion'].items():
        if k in positive:
            pos += v
        else:
            neg += v
            
    return ("positive", pos) if pos > neg else ("negative", neg)

def read_image_as_cv2(image_file):
    # Convert the image from Flask file object to a format usable by OpenCV
    img = Image.open(image_file.stream).convert('RGB')
    np_img = np.array(img)
    cv2_img = cv2.cvtColor(np_img, cv2.COLOR_RGB2BGR)
    return cv2_img



if __name__ == "__main__":
    emotions = read_image("./ck+/happy/S010_006_00000013.png")
    print(emotions)