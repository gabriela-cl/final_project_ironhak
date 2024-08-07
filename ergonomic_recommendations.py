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