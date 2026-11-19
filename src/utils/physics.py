import numpy as np

def classify_frame(ball_coords, player_boxes, ball_id):
    """
    Classifies the frame state.
    - Green (0): Normal
    - Blue (1): Merge (ball overlaps with player/bat)
    - Red (2): Drop (bounce/lowest point)
    """
    if not ball_coords:
        return 0
    
    # 1. Logic for 'Merge' (Blue)
    # Check if ball center is inside any player/bat bounding box
    bx, by = ball_coords
    for box in player_boxes:
        px1, py1, px2, py2 = box
        if px1 <= bx <= px2 and py1 <= by <= py2:
            return 1
            
    # 2. Logic for 'Drop' (Red)
    # Detect the bounce point by looking for a change in vertical velocity
    # In video coordinates, 'y' increases as the ball goes down.
    # A bounce occurs at a local maximum of 'y'.
    if len(ball_id['history']) > 2:
        y_prev = ball_id['history'][-2][1]
        y_curr = ball_id['history'][-1][1]
        # If the ball was moving down and is now moving up
        if y_prev > y_curr + 5: # Threshold to avoid noise
            return 2
            
    return 0 # Default: Normal (Green)