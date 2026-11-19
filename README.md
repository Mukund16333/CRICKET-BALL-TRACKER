# 🏏 Cricket Ball Tracker

Real-time cricket ball detection and trajectory tracking using **YOLOv8** and **OpenCV**. The system detects the cricket ball in video frames, tracks its movement, and visualizes the trajectory with color-coded trails.

## 📁 Project Structure

```
CricketBallTracker/
├── src/
│   ├── main.py              # Main pipeline with physics-based classification
│   ├── run_tracker.py        # Tracker using custom-trained model
│   ├── final_tracker.py      # Tracker using pre-trained YOLOv8n
│   └── utils/
│       ├── drawer.py         # Trajectory drawing utilities
│       ├── extract_frames.py # Video frame extraction
│       └── physics.py        # Physics-based ball state classification
├── training/
│   ├── train.py              # YOLOv8 training script
│   └── custom_data.yaml      # Training dataset configuration
├── data/
│   ├── raw/                  # Raw input videos
│   ├── processed/            # Extracted frames
│   └── dataset/              # YOLO-format training dataset
├── models/                   # Trained model weights
├── runs/                     # YOLO training outputs
├── output/                   # Tracker output files
├── dataset.yaml              # Dataset configuration
└── yolov8n.pt                # Pre-trained YOLOv8 nano weights
```

## 🚀 Features

- **Ball Detection** — YOLOv8-based real-time cricket ball detection
- **Trajectory Tracking** — Persistent ball path visualization across frames
- **Physics Classification** — State-based tracking (in-flight, bounce, caught, etc.)
- **Custom Training** — Fine-tune YOLOv8 on custom cricket ball datasets
- **Color-Coded Trails** — Visual trajectory with state-dependent coloring

## 🛠️ Tech Stack

- **Python 3.x**
- **[Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics)** — Object detection
- **OpenCV** — Video processing & visualization
- **PyTorch** — Deep learning backend

## ⚙️ Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/CRICKET-BALL-TRACKER.git
   cd CRICKET-BALL-TRACKER
   ```

2. **Install dependencies**
   ```bash
   pip install ultralytics opencv-python
   ```

3. **Place your video** in `data/raw/`

4. **Run the tracker**
   ```bash
   # Using pre-trained YOLOv8n
   python src/final_tracker.py

   # Using custom-trained model
   python src/run_tracker.py
   ```

## 🏋️ Training

To train YOLOv8 on your own cricket ball dataset:

1. Organize your dataset in YOLO format under `data/dataset/`
2. Update `training/custom_data.yaml` with your dataset paths
3. Run training:
   ```bash
   python training/train.py
   ```

Trained weights will be saved to `runs/detect/train/weights/best.pt`.

## 📄 License

This project is licensed under the [MIT License](LICENSE).

