import cv2
from ultralytics import YOLO
from utils.physics import classify_frame
from utils.drawer import draw_trajectory

# Load your fine-tuned model
model = YOLO('models/yolov8_ball.pt') 
cap = cv2.VideoCapture('data/raw/match_video.mp4')

# Persistent storage for the ball's path
# Each item: (x, y, state)
ball_path = [] 

while cap.isOpened():
    success, frame = cap.read()
    if not success: break

    # 1. Run Detection
    results = model(frame)[0]
    
    current_ball = None
    player_boxes = []
    
    for box in results.boxes:
        cls = int(box.cls[0])
        coords = box.xyxy[0].tolist()
        
        if cls == 0: # Assuming Class 0 is 'Ball'
            current_ball = ((coords[0]+coords[2])/2, (coords[1]+coords[3])/2)
        elif cls == 1: # Assuming Class 1 is 'Player'
            player_boxes.append(coords)

    # 2. Classify and Update Trajectory
    if current_ball:
        state = classify_frame(current_ball, player_boxes, {'history': [p[:2] for p in ball_path]})
        ball_path.append((*current_ball, state))
    
    # Keep trail length manageable (e.g., last 50 frames)
    if len(ball_path) > 50: ball_path.pop(0)

    # 3. Draw and Show
    annotated_frame = draw_trajectory(frame, ball_path)
    cv2.imshow("Cricket Tracking", annotated_frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'): break

cap.release()
cv2.destroyAllWindows()