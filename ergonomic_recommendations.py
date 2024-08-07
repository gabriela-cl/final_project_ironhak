results = pose.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

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
        print("Detected Left Side")
        hip_angle = left_hip_angle
        knee_angle = left_knee_angle
        elbow_angle = left_elbow_angle
        
        print(f'Hip Angle: {left_hip_angle:.2f} degrees')
        print(f'Knee Angle: {left_knee_angle:.2f} degrees')
        print(f'Elbow Angle: {left_elbow_angle:.2f} degrees')
    else:
        print("Detected Right Side")
        hip_angle = right_hip_angle
        knee_angle = right_knee_angle
        elbow_angle = right_elbow_angle
        print(f'Hip Angle: {right_hip_angle:.2f} degrees')
        print(f'Knee Angle: {right_knee_angle:.2f} degrees')
        print(f'Elbow Angle: {right_elbow_angle:.2f} degrees')




def ergonomic_analysis(elbow_angle, hip_angle, knee_angle):
    recommendations = []

    # Elbow Angle
    if elbow_angle < 90:
        recommendations.append("Raise chair or lower desk to increase elbow angle.")
    elif elbow_angle > 120:
        recommendations.append("Lower chair or raise desk to decrease elbow angle.")

    # Hip Angle
    if hip_angle < 90:
        recommendations.append("Raise chair to increase hip angle. Consider using a footrest.")
    elif hip_angle > 120:
        recommendations.append("Lower chair to decrease hip angle.")

    # Knee Angle
    if knee_angle < 90:
        recommendations.append("Raise chair to increase knee angle. Ensure feet are flat on the floor or use a footrest.")
    elif knee_angle > 130:
        recommendations.append("Lower chair to decrease knee angle.")

    # Output recommendations
    if not recommendations:
        return "All angles are within recommended ranges. No adjustments needed."
    else:
        return recommendations

result = ergonomic_analysis(elbow_angle, hip_angle, knee_angle)
for recommendation in result:
    print(recommendation)