import cv2
import librosa
import numpy as np




def preprocess_image(img_path):
    img = cv2.imread(img_path)
    resized = cv2.resize(img, (224, 224))
    hsv = cv2.cvtColor(resized, cv2.COLOR_BGR2HSV)
    return hsv
def extract_audio_features(path):
    y, sr = librosa.load(path, sr=16000)
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
    return np.mean(mfcc, axis=1)