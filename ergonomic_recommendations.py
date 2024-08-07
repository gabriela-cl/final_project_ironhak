{\rtf1\ansi\ansicpg1252\cocoartf2761
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 def ergonomic_analysis(elbow_angle, hip_angle, knee_angle):\
    recommendations = []\
\
    # Elbow Angle\
    if elbow_angle < 90:\
        recommendations.append("Raise chair or lower desk to increase elbow angle.")\
    elif elbow_angle > 120:\
        recommendations.append("Lower chair or raise desk to decrease elbow angle.")\
\
    # Hip Angle\
    if hip_angle < 90:\
        recommendations.append("Raise chair to increase hip angle. Consider using a footrest.")\
    elif hip_angle > 120:\
        recommendations.append("Lower chair to decrease hip angle.")\
\
    # Knee Angle\
    if knee_angle < 90:\
        recommendations.append("Raise chair to increase knee angle. Ensure feet are flat on the floor or use a footrest.")\
    elif knee_angle > 130:\
        recommendations.append("Lower chair to decrease knee angle.")\
\
    # Output recommendations\
    if not recommendations:\
        return "All angles are within recommended ranges. No adjustments needed."\
    else:\
        return recommendations\
\
result = ergonomic_analysis(elbow_angle, hip_angle, knee_angle)\
for recommendation in result:\
    print(recommendation)}