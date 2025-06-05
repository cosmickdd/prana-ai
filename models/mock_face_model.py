import random

# Define your classes (adjust as needed)
FACE_CLASSES = ["normal", "vata", "pitta", "kapha"]

class MockFaceModel:
    def __init__(self):
        pass

    def predict(self, image_path):
        # Simulate prediction: randomly pick a class
        return random.choice(FACE_CLASSES)

# Example usage
if __name__ == "__main__":
    model = MockFaceModel()
    test_image = "path/to/any/image.jpg"
    prediction = model.predict(test_image)
    print(f"Predicted class: {prediction}")