# Phát hiện Xe Máy sử dụng YOLOv8

Dự án này sử dụng YOLOv8 (You Only Look Once phiên bản 8) để phát hiện xe máy trong video. Hệ thống phát hiện xe máy từ một video đã cho và đếm số lượng xe máy theo thời gian thực. Điều này có thể hữu ích cho việc giám sát giao thông, an ninh và quy hoạch đô thị.

## Tính năng
- Tải mô hình YOLOv8 đã được huấn luyện sẵn để phát hiện đối tượng.
- Xử lý các khung hình video và phát hiện xe máy với độ chính xác cao.
- Hiển thị video với các hộp bao quanh xe máy được phát hiện.
- Đếm xe máy theo thời gian thực hiển thị trên video.
- Lưu video đầu ra với kết quả phát hiện.

## Yêu cầu
Để chạy dự án, bạn cần cài đặt các phiên bản phần mềm sau:
- Python 3.7+
- OpenCV 4.5+
- PyTorch 1.10+
- Ultralytics YOLOv8

Bạn có thể cài đặt các phụ thuộc bằng cách chạy lệnh sau:

```bash
pip install -r requirements.txt
```


## Cài đặt
Để thiết lập dự án trên máy tính của bạn, làm theo các bước sau:
1. Clone kho lưu trữ:

```bash
git clone https://github.com/Nguyen-Van-Chan/motorcycle-detection-yolov8.git 
cd motorcycle-detection-yolov8
```

2. Cài đặt các phụ thuộc cần thiết:

```bash
pip install -r requirements.txt
```

3. Tải tệp mô hình YOLOv8:
- Truy cập trang [Ultralytics YOLOv8 GitHub releases page](https://github.com/ultralytics/yolov8/releases) để tải mô hình phù hợp.
- Đặt mô hình đã tải (ví dụ: `yolov8x.pt`) vào thư mục `model/` của dự án.
## Cách sử dụng

### Bước 1: Chuẩn bị Video và Mô Hình
Đảm bảo bạn có một tệp video (ví dụ: `cauBinhTrieu.mp4`) chứa cảnh quay xe máy. Đặt video này vào thư mục dự án.

### Bước 2: Sửa đổi Cấu hình
Đảm bảo rằng các biến cấu hình sau đã được thiết lập chính xác trong `main.py`:
- **video_path**: Đặt đường dẫn đến tệp video của bạn. Mặc định là `cauBinhTrieu.mp4`.
- **model_path**: Đặt đường dẫn đến mô hình YOLOv8 mà bạn đã tải xuống (ví dụ: `model/yolov8x.pt`).
- **confidence_threshold**: Điều chỉnh ngưỡng độ tin cậy cho phát hiện (mặc định là 0.5).

### Bước 3: Chạy Script
Chạy script để bắt đầu quá trình phát hiện:

```bash
python main.py
```


## Chuyện gì sẽ xảy ra tiếp theo?
Khi script đang chạy:

- Chương trình sẽ hiển thị video với các xe máy được phát hiện, hiển thị hộp bao quanh từng chiếc xe máy.
- Số lượng xe máy phát hiện được sẽ được hiển thị trên video theo thời gian thực.
- Nhấn `q` để dừng phát video.
- Video đầu ra với kết quả phát hiện sẽ được lưu lại dưới tên `output.mp4` trong thư mục dự án.

## Tùy chỉnh
Bạn có thể tùy chỉnh các khía cạnh sau của dự án:

### Ngưỡng Độ Tin Cậy
Bạn có thể điều chỉnh ngưỡng độ tin cậy cho phát hiện bằng cách thay đổi biến `confidence_threshold` trong `main.py`. Giá trị mặc định là `0.5`. Các giá trị cao hơn sẽ dẫn đến ít phát hiện hơn nhưng có độ chính xác cao hơn.

### Tệp Video
Nếu bạn muốn sử dụng một video khác, chỉ cần thay đổi giá trị của biến `video_path` thành đường dẫn đến tệp video mới của bạn.

### Lựa chọn Mô Hình
Bạn có thể thử nghiệm với các mô hình YOLOv8 khác nhau (ví dụ: `yolov8s.pt`, `yolov8m.pt`, `yolov8x.pt`) bằng cách thay đổi biến `model_path` trong tệp `main.py`.

## Đóng góp
Chúng tôi chào đón sự đóng góp từ cộng đồng! Để đóng góp:

1. Fork kho lưu trữ.
2. Tạo một nhánh mới.
3. Thực hiện các thay đổi của bạn.
4. Gửi một pull request với mô tả về các thay đổi của bạn.

## Giấy phép
Dự án này được cấp phép theo Giấy phép MIT. Xem tệp `LICENSE` để biết chi tiết.

## Lời cảm ơn
- Cảm ơn đội ngũ [Ultralytics](https://github.com/ultralytics) đã cung cấp mô hình YOLOv8.
- Đặc biệt cảm ơn cộng đồng OpenCV và PyTorch vì các thư viện tuyệt vời của họ.

## Liên hệ
Nếu có bất kỳ câu hỏi hoặc vấn đề nào, vui lòng liên hệ:

[Your Name]  
Email: [support@techspherex.com]  
GitHub: [https://github.com/Nguyen-Van-Chan](https://github.com/Nguyen-Van-Chan)