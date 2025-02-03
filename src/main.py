from datetime import datetime
import cv2
import torch
from ultralytics import YOLO


def load_model(model_path):
    """
    Tải mô hình YOLO từ đường dẫn chỉ định.
    """
    return YOLO(model_path)


def process_frame(frame, model, confidence_threshold):
    """
    Xử lý một frame và phát hiện xe máy bằng mô hình YOLO.
    
    Args:
        frame (ndarray): Frame cần xử lý.
        model (YOLO): Mô hình YOLO để phát hiện.
        confidence_threshold (float): Ngưỡng độ tin cậy để lọc kết quả.

    Returns:
        tuple: Frame đã được xử lý, số lượng xe máy phát hiện được.
    """
    results = model(frame)
    motorbike_count = 0
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 0.5
    font_color = (0, 255, 0)  # Màu xanh lá
    thickness = 1

    for result in results:
        boxes = result.boxes  # Hộp giới hạn (bounding boxes)
        for box in boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            class_id = int(box.cls[0])
            confidence = float(box.conf[0])  # Lấy giá trị độ tin cậy

            class_name = model.names[class_id]

            # Lọc kết quả cho xe máy với độ tin cậy đủ lớn
            if class_name.lower() == 'motorcycle' and confidence >= confidence_threshold:
                motorbike_count += 1
                label = f"{class_name} {confidence:.2f}"
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)  # Hộp màu xanh lá
                cv2.putText(frame, label, (x1, y1 - 10), font, font_scale, font_color, thickness)

    return frame, motorbike_count


def display_video(video_path, model, confidence_threshold):
    """
    Hiển thị video kèm phát hiện xe máy và đếm theo thời gian thực.

    Args:
        video_path (str): Đường dẫn tới file video.
        model (YOLO): Mô hình YOLO để phát hiện đối tượng.
        confidence_threshold (float): Ngưỡng độ tin cậy để lọc kết quả.
    """
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Lỗi: Không thể mở file video.")
        return

    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 2  # Tăng kích thước chữ
    font_color = (0, 255, 0)  # Màu xanh lá
    thickness = 2  # Tăng độ dày chữ

    while True:
        ret, frame = cap.read()
        if not ret:
            break  # Thoát vòng lặp nếu không còn frame nào

        # Xử lý frame và đếm số lượng xe máy
        frame, motorbike_count = process_frame(frame, model, confidence_threshold)

        # Hiển thị số lượng xe máy trên frame
        cv2.putText(frame, f"Motorbikes: {motorbike_count}", (10, 50), font, font_scale, font_color, thickness)

        # Thay đổi kích thước và hiển thị frame
        output_width, output_height = 1080, 720
        frame = cv2.resize(frame, (output_width, output_height))
        filename = f'debugs/{datetime.now().strftime("%Y_%m_%d_%H_%M_%S")}.png'
        cv2.imwrite(filename, frame)
        cv2.imshow('YOLOv8 Detection', frame)

        # Thoát chương trình khi nhấn phím 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


def main():
    """
    Hàm chính để chạy chương trình phát hiện xe máy bằng YOLOv8.
    """
    model_path = 'model/yolov8x.pt'
    video_path = 'cauBinhTrieu.mp4'
    confidence_threshold = 0.5

    print("Đang tải mô hình YOLO...")
    model = load_model(model_path)

    print("Bắt đầu phát hiện video...")
    display_video(video_path, model, confidence_threshold)


if __name__ == "__main__":
    main()
