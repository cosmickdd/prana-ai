import cv2
import numpy as np
import tensorflow as tf
import random


def analyze_lips(img):
    classes = ["normal", "cracked_dry", "reddish"]
    return {
        "prediction": random.choice(classes),
        "confidence": round(random.uniform(0.7, 0.99), 2)
    }