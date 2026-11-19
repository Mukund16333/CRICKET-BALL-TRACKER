import cv2
from ultralytics import YOLO

model = YOLO('runs/detect/train/weights/best.pt') # The "brain" created by training
cap = cv2.VideoCapture('data/raw/test_video.mp4')
path_history = [] # To store (x, y, color)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret: break

    results = model(frame)[0]
    ball_pos = None
    
    # Logic to find the ball and determine color
    for box in results.boxes:
        coords = box.xyxy[0].tolist()
        label = model.names[int(box.cls[0])]
        
        if label == 'ball':
            ball_pos = (int((coords[0]+coords[2])/2), int((coords[1]+coords[3])/2))
            color = (0, 255, 0) # Default Green
            
            # Change to Red if near bottom (Drop) or Blue if near player (Merge)
            # Add your physics logic here!
            path_history.append((ball_pos, color))

    # Draw the tail
    for i in range(1, len(path_history)):
        cv2.line(frame, path_history[i-1][0], path_history[i][0], path_history[i][1], 2)

    cv2.imshow('Cricket Tracker', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'): break

cap.release()
cv2.destroyAllWindows()