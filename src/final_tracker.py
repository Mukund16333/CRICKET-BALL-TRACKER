import cv2
from ultralytics import YOLO

# 1. Load the pre-trained model for guaranteed results
model = YOLO('yolov8n.pt') 

# 2. Use the exact path to your video
video_path = r'C:\Users\MUKUND BALAJI B\CricketBallTracker\data\raw\test_video.mp4'
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Could not open video. Check the path!")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # 3. Run detection (conf=0.25 is standard)
    results = model(frame, conf=0.25)[0]
    
    # 4. CRITICAL: This 'plots' the boxes onto a NEW frame
    annotated_frame = results.plot() 

    # 5. Show the ANNOTATED frame, not the original 'frame'
    cv2.imshow('FINAL PROJECT SUBMISSION', annotated_frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
print("Process Finished.")