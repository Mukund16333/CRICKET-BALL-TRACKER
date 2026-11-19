import cv2
import os

def extract_frames(video_name, interval=5):
    # 1. Automatically find the Project Root (CricketBallTracker)
    # This works even if you run the script from inside src/utils
    base_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.abspath(os.path.join(base_dir, "..", ".."))
    
    # 2. Setup Absolute Paths
    video_path = os.path.join(project_root, 'data', 'raw', f"{video_name}.mp4")
    output_folder = os.path.join(project_root, 'data', 'processed')
    
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        
    # 3. Open Video and Validate
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"Error: Could not open video at {video_path}")
        return

    count, saved_count = 0, 0
    print("Starting extraction...")

    while True:
        ret, frame = cap.read()
        if not ret:
            break # End of video
        
        # 4. Save frames at the specified interval
        if count % interval == 0:
            frame_path = os.path.join(output_folder, f"frame_{saved_count:04d}.jpg")
            cv2.imwrite(frame_path, frame)
            saved_count += 1
        
        count += 1
        # Progress update every 100 frames
        if count % 100 == 0:
            print(f"Processed {count} frames...")

    cap.release()
    print(f"Successfully extracted {saved_count} frames to: {output_folder}")

if __name__ == "__main__":
    # Just use the name of your file (without .mp4)
    extract_frames('test_video')