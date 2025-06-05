import os
import cv2
import pytesseract
from PIL import Image

# Load Haar cascade face detector
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# CONFIG: change this to your actual dataset root
root_dir = "data"  # e.g., "C:/Users/YourName/Desktop/ayurveda_images"

# Filter thresholds (relaxed)
TEXT_THRESHOLD = 100   # Allow more text
MIN_SIZE = 32          # Minimum width/height

# Check if image is large enough
def is_large_enough(image_path, min_size=MIN_SIZE):
    try:
        img = Image.open(image_path)
        return img.width >= min_size and img.height >= min_size
    except:
        return False

# Check if image has too much text using OCR (relaxed)
def has_excess_text(image_path, threshold=TEXT_THRESHOLD):
    try:
        img = cv2.imread(image_path)
        if img is None:
            return True
        text = pytesseract.image_to_string(img)
        return len(text.strip()) > threshold
    except:
        return True

# Check if image contains a face (for 'face' folder only)
def contains_face(image_path):
    try:
        img = cv2.imread(image_path)
        if img is None:
            return False
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        return len(faces) > 0
    except:
        return False

# Clean all images in subfolders
def clean_dataset(root):
    removed = 0
    for trait in os.listdir(root):
        trait_path = os.path.join(root, trait)
        if not os.path.isdir(trait_path): continue
        for cls in os.listdir(trait_path):
            class_path = os.path.join(trait_path, cls)
            if not os.path.isdir(class_path): continue
            for img_file in os.listdir(class_path):
                img_path = os.path.join(class_path, img_file)
                try:
                    # Only keep images that are large enough and not too much text
                    if (not is_large_enough(img_path)) or has_excess_text(img_path) or \
                       (trait == "face" and not contains_face(img_path)):
                        os.remove(img_path)
                        removed += 1
                except:
                    os.remove(img_path)
                    removed += 1
    print(f"✅ Cleaning complete. Removed {removed} bad images.")

# Run it
if __name__ == "__main__":
    clean_dataset(root_dir)
