# Motorcycle Detection using YOLOv8

This project uses YOLOv8 (You Only Look Once version 8) for detecting motorcycles in videos. The system detects motorbikes from a given video and counts them in real-time. This can be useful for traffic monitoring, security, and urban planning.

## Features
- Load a pre-trained YOLOv8 model for object detection.
- Process video frames and detect motorcycles with high accuracy.
- Display the video with bounding boxes around detected motorcycles.
- Real-time counting of motorcycles displayed on the video.
- Save the output video with detection results.

## Requirements
To run the project, you'll need the following software versions installed:
- Python 3.7+
- OpenCV 4.5+
- PyTorch 1.10+
- Ultralytics YOLOv8

You can install the dependencies by running the following command:


```bash
pip install -r requirements.txt
```

## Installation
To set up the project locally, follow these steps:

1. Clone the repository:

```bash
git clone https://github.com/Nguyen-Van-Chan/motorcycle-detection-yolov8.git 
cd motorcycle-detection-yolov8
```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```


3. Download the YOLOv8 model file:
- Visit the [Ultralytics YOLOv8 GitHub releases page](https://github.com/ultralytics/yolov8/releases) to download the appropriate model.
- Place the downloaded model (e.g., `yolov8x.pt`) in the `model/` directory of the project.

## Usage

### Step 1: Prepare Video and Model
Make sure you have a video file (e.g., `cauBinhTrieu.mp4`) that contains motorcycle footage. Place this video in the project directory.

### Step 2: Modify Configuration
Ensure that the following configuration variables are set correctly in `main.py`:

- **video_path**: Set the path to your video file. Default is `cauBinhTrieu.mp4`.
- **model_path**: Set the path to the YOLOv8 model you downloaded (e.g., `model/yolov8x.pt`).
- **confidence_threshold**: Adjust the confidence threshold for detection (default is 0.5).

### Step 3: Run the Script
Run the script to start the detection process:

```bash
python main.py
```


## What Happens Next?
Once the script is running:

- The program will display the video with detected motorcycles, showing bounding boxes around each detected motorcycle.
- The count of detected motorcycles will be displayed on the video in real-time.
- Press `q` to stop the video playback.
- The output video with detection results will be saved as `output.mp4` in the project directory.

## Customization
You can customize the following aspects of the project:

### Confidence Threshold
You can adjust the confidence threshold for detection by modifying the `confidence_threshold` variable in `main.py`. The default value is `0.5`. Higher values will result in fewer detections but higher accuracy.

### Video File
If you want to use a different video, simply change the value of the `video_path` variable to the path of your new video file.

### Model Selection
You can experiment with different YOLOv8 models (e.g., `yolov8s.pt`, `yolov8m.pt`, `yolov8x.pt`) by changing the `model_path` variable in the `main.py` file.

## Contributing
Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Submit a pull request with a description of your changes.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgments
- Thanks to the [Ultralytics team](https://github.com/ultralytics) for providing the YOLOv8 model.
- Special thanks to the OpenCV and PyTorch communities for their excellent libraries.

## Contact
For any questions or issues, please contact:

Email: [support@techspherex.com]  
GitHub: [https://github.com/Nguyen-Van-Chan](https://github.com/Nguyen-Van-Chan)
