import cv2
import numpy as np
import tensorflow as tf
import random


def analyze_tongue(img):
    classes = ["normal", "pale", "coated", "red"]
    return {
        "prediction": random.choice(classes),
        "confidence": round(random.uniform(0.7, 0.99), 2)
    }
