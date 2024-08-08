
#recommendations test:
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






#function for recommendations if the desk is not adjustable: ergonomic_analysis_fixed_desk(elbow_angle, hip_angle, knee_angle)
def ergonomic_analysis_fixed_desk(elbow_angle, hip_angle, knee_angle):
    recommendations = []
    
    #Hip Angle: Small (hip_angle < 90)
    if hip_angle < 90 and knee_angle < 90 and elbow_angle < 90
        recommendations.append("Raise your chair to increase knee, hip and elbow angles.")
    elif hip_angle < 90 and knee_angle < 90 and 90 =< elbow_angle =< 120
        recommendations.append("Raise your chair to increase knee and hip angles. Your elbow angle is okay.")
    elif hip_angle < 90 and knee_angle < 90 and elbow_angle > 120
        recommendations.append("Raise your chair to increase knee and hip angles.\nConsider getting closer to the desk or lowering the chair armrest to decrease the elbow angle.")
    elif hip_angle < 90 and 90 =< knee_angle =< 130 and elbow_angle < 90
        recommendations.append("Raise your chair to increase hip and elbow angles, make sure your feet are under your knee for the analysis.\nIf your feet are not resting on the floor after the adjustment, consider to add a footrest.")
    elif hip_angle < 90 and 90 =< knee_angle =< 130 and 90 =< elbow_angle =< 120
        recommendations.append("Raise your chair to increase hip angle. Your knee and elbow angles are okay.\nMake sure your feet are under your knee and your back is resting on a vertical position for the analysis.\nIf your feet are not resting on the floor after the adjustment, consider to add a footrest.")
    elif hip_angle < 90 and 90 =< knee_angle =< 130 and elbow_angle > 120
        recommendations.append("Raise your chair to increase hip angle.\nConsider getting closer to the desk or lowering the chair armrest to decrease the elbow angle.\nYour knee angle is okay. Make sure your feet are under your knee and your back is resting on a vertical position for the analysis.\nIf your feet are not resting on the floor after the adjustment, consider to add a footrest.")
    elif hip_angle < 90 and knee_angle > 130 and elbow_angle < 90
        recommendations.append("Raise your chair to increase hip and elbow angles, make sure your feet are under your knee and your back is resting on a vertical position for the analysis.\nIf your feet are not resting on the floor after the adjustment, consider to add a footrest.")
    elif hip_angle < 90 and knee_angle > 130 and 90 =< elbow_angle =< 120
        recommendations.append("Raise your chair to increase hip angle, make sure your feet are under your knee and your back is resting on a vertical position for the analysis.\nIf your feet are not resting on the floor after the adjustment, consider to add a footrest.\nYour elbow angle is okay.")
    elif hip_angle < 90 and knee_angle > 130 and elbow_angle > 120
        recommendations.append("Raise your chair to increase hip angle.\nConsider getting closer to the desk or lowering the chair armrest to decrease the elbow angle.\nMake sure your feet are under your knee for the analysis. If your feet are not resting on the floor after the adjustment, consider to add a footrest.")

    #Hip Angle: Normal (90 ≤ hip_angle ≤ 120)
    elif 90 =< hip_angle =< 120 and knee_angle < 90 and elbow_angle < 90
        recommendations.append("Raise your chair to increase knee and elbow angles, your hip angle is okay.")
    elif 90 =< hip_angle =< 120 and knee_angle < 90 and 90 =< elbow_angle =< 120
        recommendations.append("Make sure your feet are under your knee for the analysis, raise your chair to increase knee angle if necessary.\nYour hip and elbow angles are okay.")
    elif 90 =< hip_angle =< 120 and knee_angle < 90 and elbow_angle > 120
        recommendations.append("Raise your chair to increase knee angle.\nConsider getting closer to the desk or lowering the chair armrest to decrease the elbow angle.\nYour hip angle is okay.")
    elif 90 =< hip_angle =< 120 and 90 =< knee_angle =< 130 and elbow_angle < 90
        recommendations.append("Raise your chair to increase elbow angle.\nConsider adding a footrest to keep the knee and hip angles within the recommended ranges.")
    #elif 90 =< hip_angle =< 120 and 90 =< knee_angle =< 130 and 90 =< elbow_angle =< 120
        #recommendations.append("All angles are within recommended ranges. No adjustments needed.")
    elif 90 =< hip_angle =< 120 and 90 =< knee_angle =< 130 and elbow_angle > 120
        recommendations.append("Yor knee and hip angles are okay.\nConsider getting closer to the desk or lowering the chair armrest to decrease the elbow angle.")
    elif 90 =< hip_angle =< 120 and knee_angle > 130 and elbow_angle < 90
        recommendations.append("Raise your chair to increase elbow angle.\nConsider adding a footrest to decrease the knee angle.\nYour hip angle is okay.")
    elif 90 =< hip_angle =< 120 and knee_angle > 130 and 90 =< elbow_angle =< 120
        recommendations.append("Make sure your feet are under your knee for the analysis. Consider adding a footrest to decrease the knee angle.\nYour hip and elbow angles are okay.")
    elif 90 =< hip_angle =< 120 and knee_angle > 130 and elbow_angle > 120
        recommendations.append("Lower your chair to decrease knee and elbow angles, your hip angle is okay.")

    #Hip Angle: Large (hip_angle > 120)
    elif hip_angle > 120 and knee_angle < 90 and elbow_angle < 90
        recommendations.append("Raise the chair to increase knee and elbow angles.\nMake sure hip is as back as possible on the chair sit and your back is resting on a vertical position.\nIf necessary add a pillow behind your lower back to decrease the hip angle.")
    elif hip_angle > 120 and knee_angle < 90 and 90 =< elbow_angle =< 120
        recommendations.append("Raise the chair to increase knee angle.\nIf necessary add a pillow behind your lower back to decrease the hip angle.\nYour elbow angle is okay.")
    elif hip_angle > 120 and knee_angle < 90 and elbow_angle > 120
        recommendations.append("Raise the chair to increase knee angle.\nIf necessary add a pillow behind your lower back to decrease the hip angle.\nConsider getting closer to the desk or lowering the chair armrest to decrease the elbow angle.")
    elif hip_angle > 120 and 90 =< knee_angle =< 130 and elbow_angle < 90
        recommendations.append("Raise the chair to increase elbow angle.\nYor knee angle is within the recommended angles, consider adding a footrest after the adjustments to decrease knee and hip angles.\nAdd a pillow behind your lower back if necessary.")
    elif hip_angle > 120 and 90 =< knee_angle =< 130 and 90 =< elbow_angle =< 120
        recommendations.append("Add a pillow or a support behind your lower back to decrease the hip angle.\nYor knee and elbow angles are okay.")
    elif hip_angle > 120 and 90 =< knee_angle =< 130 and elbow_angle > 120
        recommendations.append("Add a pillow behind your lower back to decrease elbow and hip angles. If necessary, lower your chair.\nYor knee angle is within the recommended angles, please review it if you made adjustments in the chair's hight.")
    elif hip_angle > 120 and knee_angle > 130 and elbow_angle < 90
        recommendations.append("Raise the chair to increase elbow angle.\nAdd a footrest to decrease knee and hip angles.")
    elif hip_angle > 120 and knee_angle > 130 and 90 =< elbow_angle =< 120
        recommendations.append("Add a footrest to decrease knee and hip angles.\nYour elbow angle is okay.")
    elif hip_angle > 120 and knee_angle > 130 and elbow_angle > 120
        recommendations.append("Lower the chair to decrease knee, hip and elbow angles")

    # Output recommendations
    if not recommendations:
        return "All angles are within recommended ranges. No adjustments needed."
    else:
        return recommendations






#function for recommendations if the desk is adjustable: ergonomic_analysis_adjustable_desk(elbow_angle, hip_angle, knee_angle)
def ergonomic_analysis_adjustable_desk(elbow_angle, hip_angle, knee_angle):
    recommendations = []

    #Hip Angle: Small (hip_angle < 90)
    if hip_angle < 90 and knee_angle < 90 and elbow_angle < 90
        recommendations.append("Raise your chair to increase knee, hip and elbow angles.")
    elif hip_angle < 90 and knee_angle < 90 and 90 =< elbow_angle =< 120
        recommendations.append("Raise your chair to increase knee and hip angles. Your elbow angle is okay.")
    elif hip_angle < 90 and knee_angle < 90 and elbow_angle > 120
        recommendations.append("Raise your chair to increase knee and hip angles.\nRaise the desk to decrease the elbow angle.")
    elif hip_angle < 90 and 90 =< knee_angle =< 130 and elbow_angle < 90
        recommendations.append("Raise your chair to increase hip and elbow angles, make sure your feet are under your knee for the analysis.\nIf your feet are not resting on the floor after the adjustment, consider to add a footrest.")
    elif hip_angle < 90 and 90 =< knee_angle =< 130 and 90 =< elbow_angle =< 120
        recommendations.append("Raise your chair to increase hip angle. Your knee and elbow angles are okay.\nMake sure your feet are under your knee and your back is resting on a vertical position for the analysis.\nIf your feet are not resting on the floor after the adjustment, consider to add a footrest.")
    elif hip_angle < 90 and 90 =< knee_angle =< 130 and elbow_angle > 120
        recommendations.append("Raise your chair to increase hip angle.\nRaise the desk to decrease the elbow angle.\nYour knee angle is okay. Make sure your feet are under your knee and your back is resting on a vertical position for the analysis.\nIf your feet are not resting on the floor after the adjustment, consider to add a footrest.")
    elif hip_angle < 90 and knee_angle > 130 and elbow_angle < 90
        recommendations.append("Raise your chair to increase hip and elbow angles, make sure your feet are under your knee and your back is resting on a vertical position for the analysis.\nIf your feet are not resting on the floor after the adjustment, consider to add a footrest.")
    elif hip_angle < 90 and knee_angle > 130 and 90 =< elbow_angle =< 120
        recommendations.append("Raise your chair to increase hip angle, make sure your feet are under your knee and your back is resting on a vertical position for the analysis.\nIf your feet are not resting on the floor after the adjustment, consider to add a footrest.\nYour elbow angle is okay.")
    elif hip_angle < 90 and knee_angle > 130 and elbow_angle > 120
        recommendations.append("Raise your chair to increase hip angle.\nRaise the desk to decrease the elbow angle.\nMake sure your feet are under your knee for the analysis. If your feet are not resting on the floor after the adjustment, consider to add a footrest.")
   
    #Hip Angle: Normal (90 ≤ hip_angle ≤ 120)
    elif 90 =< hip_angle =< 120 and knee_angle < 90 and elbow_angle < 90
        recommendations.append("Raise your chair to increase knee and elbow angles, your hip angle is okay.")
    elif 90 =< hip_angle =< 120 and knee_angle < 90 and 90 =< elbow_angle =< 120
        recommendations.append("Make sure your feet are under your knee for the analysis, raise your chair to increase knee angle if necessary.\nYour hip and elbow angles are okay.")
    elif 90 =< hip_angle =< 120 and knee_angle < 90 and elbow_angle > 120
        recommendations.append("Raise your chair to increase knee angle.\nRaise the desk to decrease the elbow angle.\nYour hip angle is okay.")
    elif 90 =< hip_angle =< 120 and 90 =< knee_angle =< 130 and elbow_angle < 90
        recommendations.append("Lower the desk to increase elbow angle. Your knee and hip angles are okay.")
    #elif 90 =< hip_angle =< 120 and 90 =< knee_angle =< 130 and 90 =< elbow_angle =< 120
        #recommendations.append("All angles are within recommended ranges. No adjustments needed.")
    elif 90 =< hip_angle =< 120 and 90 =< knee_angle =< 130 and elbow_angle > 120
        recommendations.append("Raise the desk to decrease the elbow angle.\nYor knee and hip angles are okay.")
    elif 90 =< hip_angle =< 120 and knee_angle > 130 and elbow_angle < 90
        recommendations.append("Lower the desk to increase elbow angle.\nRaise the chair to decrease the knee angle.\nYour hip angle is okay. If needed, add a pillow behind your back after the adjustments to decrease hip angle.")
    elif 90 =< hip_angle =< 120 and knee_angle > 130 and 90 =< elbow_angle =< 120
        recommendations.append("Make sure your feet are under your knee for the analysis. Lower the chair to decrease the knee angle if needed.\nYour hip and elbow angles are okay.")
    elif 90 =< hip_angle =< 120 and knee_angle > 130 and elbow_angle > 120
        recommendations.append("Lower your chair to decrease knee and elbow angles, your hip angle is okay.")

    #Hip Angle: Large (hip_angle > 120)
    elif hip_angle > 120 and knee_angle < 90 and elbow_angle < 90
        recommendations.append("Raise the chair to increase knee and elbow angles.\nMake sure hip is as back as possible on the chair sit and your back is resting on a vertical position.\nIf necessary add a pillow behind your lower back to decrease the hip angle.")
    elif hip_angle > 120 and knee_angle < 90 and 90 =< elbow_angle =< 120
        recommendations.append("Raise the chair to increase knee angle.\nIf necessary add a pillow behind your lower back to decrease the hip angle.\nYour elbow angle is okay.")
    elif hip_angle > 120 and knee_angle < 90 and elbow_angle > 120
        recommendations.append("Raise the chair to increase knee angle.\nIf necessary add a pillow behind your lower back to decrease the hip angle.\nRaise the desk to decrease the elbow angle.")
    elif hip_angle > 120 and 90 =< knee_angle =< 130 and elbow_angle < 90
        recommendations.append("Lower the desk to increase elbow angle.\nAdd a pillow behind your lower back to decrease the hip angle.\nYor knee angle is okay.")
    elif hip_angle > 120 and 90 =< knee_angle =< 130 and 90 =< elbow_angle =< 120
        recommendations.append("Add a pillow or a support behind your lower back to decrease the hip angle.\nYor knee and elbow angles are okay.")
    elif hip_angle > 120 and 90 =< knee_angle =< 130 and elbow_angle > 120
        recommendations.append("Raise the desk to decrease elbow angle.\nAdd a pillow behind your lower back to decrease the hip angle. If necessary, lower your chair.\nYor knee angle is within the recommended angles, please review it if you made adjustments in the chair's hight.")
    elif hip_angle > 120 and knee_angle > 130 and elbow_angle < 90
        recommendations.append("Lower the chair to decrease knee and hip angles.\nLower the desk to increase elbow angle.")
    elif hip_angle > 120 and knee_angle > 130 and 90 =< elbow_angle =< 120
        recommendations.append("Add a footrest to decrease knee and hip angles.\nYour elbow angle is okay.")
    elif hip_angle > 120 and knee_angle > 130 and elbow_angle > 120
        recommendations.append("Lower the chair to decrease knee, hip and elbow angles")

    # Output recommendations
    if not recommendations:
        return "All angles are within recommended ranges. No adjustments needed."
    else:
        return recommendations
    