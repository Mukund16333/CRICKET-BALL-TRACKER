from ultralytics import YOLO

def train_model():
    # 1. Load a pretrained 'nano' model (yolov8n.pt) 
    # Smallest and fastest, good for real-time video tracking
    model = YOLO('yolov8n.pt') 

    # 2. Train the model
    # data: path to your .yaml file
    # epochs: number of training rounds
    # imgsz: resolution (multiples of 32)
    # device: 0 for GPU, 'cpu' for CPU
    results = model.train(
        data='training/custom_data.yaml', 
        epochs=100, 
        imgsz=640, 
        batch=16,
        device=0 # Change to 'cpu' if you don't have an NVIDIA GPU
    )

    print("Training complete. Weights saved to: runs/detect/train/weights/best.pt")

if __name__ == "__main__":
    train_model()