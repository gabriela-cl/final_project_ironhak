import streamlit as st
from PIL import Image
import cv2
import numpy as np
import mediapipe as mp
import ergonomic_recommendations_streamlit
import io
import os

# Initialize MediaPipe Pose
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(static_image_mode=True)
mp_drawing = mp.solutions.drawing_utils

# Title of the app
st.title("Ergonomic Recommendations: Set Up Your Workplace")

# Introductory information
st.subheader("First, we will need some information:")

# Ask the user if they have an adjustable desk
desk_adj = st.radio("Do you have an adjustable desk?", ('yes', 'no'))

# Instructions for the picture
st.subheader("Now, we will need a picture of you sitting at your work desk:")

st.write("Please make sure that your hips are as back as possible on the chair seat.")
st.write("Your back is straight, as tall as possible.")
st.write("Your feet are directly under your knee and resting on the floor.")
st.write("Keep your elbows close to your body and the wrists resting on the table.")
st.write("Take a picture from the side, try to NOT take it from a diagonal angle.")

# Display an example image
example_image_path = 'images/sitting_recommendations.png'  # Path to your example image
example_image = Image.open(example_image_path)
st.image(example_image, caption='Example: Correct Sitting Posture', use_column_width=True)

# File uploader for the user's picture
uploaded_file = st.file_uploader("Upload an image of yourself at your desk", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    # Load the uploaded image
    image = Image.open(uploaded_file)
    image = np.array(image)

    # Process the image to find pose landmarks
    results = pose.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

    # Function to calculate the angle between three points
    def calculate_angle(a, b, c):
        a = np.array(a)
        b = np.array(b)
        c = np.array(c)
        ba = a - b
        bc = c - b
        cosine_angle = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc))
        angle = np.arccos(cosine_angle)
        return np.degrees(angle)

    # Extract keypoints (landmarks) and calculate angles if landmarks are detected
    if results.pose_landmarks:
        landmarks = results.pose_landmarks.landmark

        # Extract left landmarks
        left_shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,
                         landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
        left_elbow = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,
                      landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
        left_wrist = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x,
                      landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]
        left_hip = [landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x,
                    landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y]
        left_knee = [landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].x,
                     landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].y]
        left_ankle = [landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].x,
                      landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].y]

        # Extract right landmarks
        right_shoulder = [landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x,
                          landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]
        right_elbow = [landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x,
                       landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y]
        right_wrist = [landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].x,
                       landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].y]
        right_hip = [landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].x,
                     landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].y]
        right_knee = [landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].x,
                      landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].y]
        right_ankle = [landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].x,
                       landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].y]

        # Calculate angles for the left side
        left_hip_angle = calculate_angle(left_shoulder, left_hip, left_knee)
        left_knee_angle = calculate_angle(left_hip, left_knee, left_ankle)
        left_elbow_angle = calculate_angle(left_shoulder, left_elbow, left_wrist)

        # Calculate angles for the right side
        right_hip_angle = calculate_angle(right_shoulder, right_hip, right_knee)
        right_knee_angle = calculate_angle(right_hip, right_knee, right_ankle)
        right_elbow_angle = calculate_angle(right_shoulder, right_elbow, right_wrist)

        # Determine which side is more visible based on confidence scores
        if landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].visibility > landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].visibility:
            hip_angle = left_hip_angle
            knee_angle = left_knee_angle
            elbow_angle = left_elbow_angle
        else:
            hip_angle = right_hip_angle
            knee_angle = right_knee_angle
            elbow_angle = right_elbow_angle

        # Call the appropriate function based on the desk type
        if desk_adj == 'yes':
            result = ergonomic_recommendations_streamlit.ergonomic_analysis_adjustable_desk(elbow_angle, hip_angle, knee_angle)
        elif desk_adj == 'no':
            result = ergonomic_recommendations_streamlit.ergonomic_analysis_fixed_desk(elbow_angle, hip_angle, knee_angle)
        
        # Display the recommendations
        for recommendation in result:
            st.write(recommendation)

    # Display the uploaded image
    st.image(image, caption='Uploaded Image', use_column_width=True)