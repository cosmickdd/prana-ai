import cv2
import numpy as np
import tensorflow as tf
import random



def analyze_nails(img):
    classes = ["normal", "bluish", "reddish", "pale"]
    return {
        "prediction": random.choice(classes),
        "confidence": round(random.uniform(0.7, 0.99), 2)
    }