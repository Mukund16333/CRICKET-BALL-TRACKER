import cv2
import numpy as np

def draw_trajectory(frame, trajectory_points):
    """
    trajectory_points: List of tuples (x, y, state)
    States: 0=Green, 1=Blue, 2=Red
    """
    colors = {0: (0, 255, 0), 1: (255, 0, 0), 2: (0, 0, 255)}
    
    # Draw lines between consecutive points
    for i in range(1, len(trajectory_points)):
        pt1 = (int(trajectory_points[i-1][0]), int(trajectory_points[i-1][1]))
        pt2 = (int(trajectory_points[i][0]), int(trajectory_points[i][1]))
        state = trajectory_points[i][2]
        
        # Use a thicker line for the 'Drop' or 'Merge' for visibility
        thickness = 5 if state > 0 else 2
        cv2.line(frame, pt1, pt2, colors[state], thickness)
        
    return frame