import streamlit as st
from inference.face_analysis import analyze_face
from inference.tongue_analysis import analyze_tongue
from inference.lips_analysis import analyze_lips
from inference.nail_analysis import analyze_nails
import numpy as np
import cv2
import time

st.set_page_config(page_title="Ayurvedic AI", page_icon="🌿", layout="centered")

steps = [
    {"label": "Face", "instruction": "Center your face in the camera. Look straight ahead."},
    {"label": "Tongue", "instruction": "Stick out your tongue and center it in the camera."},
    {"label": "Lips", "instruction": "Relax your lips and center them in the camera."},
    {"label": "Nails", "instruction": "Show your nails clearly to the camera."}
]

# Onboarding
if "onboarded" not in st.session_state:
    st.session_state.onboarded = False

if not st.session_state.onboarded:
    st.title("🌿 Welcome to PRANA AI")
    st.markdown("""
    This app will guide you through a quick visual health analysis using your webcam.
    
    **How it works:**
    1. You'll be guided step-by-step to capture images of your face, tongue, lips, and nails.
    2. After each capture, our AI will analyze your image and automatically move to the next step.
    3. At the end, you'll see a summary of your results.
    """)
    if st.button("Start Analysis"):
        st.session_state.onboarded = True
        st.session_state.step = 0
        st.session_state.captures = [None] * len(steps)
        st.session_state.results = [None] * len(steps)
        st.rerun()
    st.stop()

# Initialize session state
if "step" not in st.session_state:
    st.session_state.step = 0
if "captures" not in st.session_state:
    st.session_state.captures = [None] * len(steps)
if "results" not in st.session_state:
    st.session_state.results = [None] * len(steps)

step = st.session_state.step

st.progress((step+1)/len(steps), text=f"Step {step+1} of {len(steps)}: {steps[step]['label']}")

st.header(f"Step {step+1}: {steps[step]['label']}")
st.info(steps[step]["instruction"])

img_file = st.camera_input(f"Capture {steps[step]['label']} Image")

if img_file is not None and st.session_state.captures[step] is None:
    # Convert to OpenCV image
    file_bytes = np.asarray(bytearray(img_file.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, 1)
    st.session_state.captures[step] = img

    # Analyze based on step
    if step == 0:
        result = analyze_face(img)
    elif step == 1:
        result = analyze_tongue(img)
    elif step == 2:
        result = analyze_lips(img)
    elif step == 3:
        result = analyze_nails(img)
    else:
        result = {}

    st.session_state.results[step] = result

    st.success(f"Prediction: {result['prediction']} (Confidence: {result['confidence']*100:.1f}%)")
    st.write("Analyzing... Moving to next step.")
    time.sleep(2)  # Short pause for user to see result

    # Auto-advance to next step
    if step < len(steps) - 1:
        st.session_state.step += 1
        st.rerun()
    else:
        st.session_state.completed = True
        st.rerun()

# Unboarding / Results
if st.session_state.get("completed", False):
    st.balloons()
    st.title("🎉 Analysis Complete!")
    st.markdown("Here are your Ayurvedic AI results:")
    for i, step_info in enumerate(steps):
        result = st.session_state.results[i]
        st.write(f"**{step_info['label']}**: {result['prediction']} (Confidence: {result['confidence']*100:.1f}%)")
    st.markdown("---")
    if st.button("Restart"):
        for key in ["onboarded", "step", "captures", "results", "completed"]:
            if key in st.session_state:
                del st.session_state[key]
        st.rerun()

# Allow user to go back if needed
if step > 0 and not st.session_state.get("completed", False):
    if st.button("Previous Step"):
        st.session_state.captures[step] = None
        st.session_state.results[step] = None
        st.session_state.step -= 1
        st.rerun()
