import random

def analyze_face(img):
    classes = ["normal", "vata", "pitta", "kapha"]
    return {
        "prediction": random.choice(classes),
        "confidence": round(random.uniform(0.7, 0.99), 2)
    }