# ỨNG DỤNG NHẬN DIỆN ĐỘNG VẬT BẰNG MÔ HÌNH MOBILENETV2

Ứng dụng web cho phép người dùng tải lên hình ảnh và nhận diện các loài động vật sử dụng mô hình Deep Learning MobileNetV2. Ứng dụng được xây dựng bằng Flask và TensorFlow, với giao diện web đơn giản và dễ sử dụng.

## Tính năng chính

- Nhận diện nhiều loài động vật khác nhau từ hình ảnh
- Giao diện web thân thiện với người dùng
- Sử dụng mô hình MobileNetV2 đã được huấn luyện trước
- Hỗ trợ tải lên hình ảnh từ máy tính

## Hướng dẫn cài đặt

1. Clone repository và tạo môi trường ảo:
    ```bash
    python -m venv venv
    .\venv\Scripts\Activate
    ```

2. Cài đặt các thư viện cần thiết:
    ```bash
    pip install flask numpy pillow tensorflow keras werkzeug
    ```

3. Thư viện bổ sung cho huấn luyện mô hình (tùy chọn):
    ```bash
    pip install matplotlib kaggle
    ```

## Hướng dẫn sử dụng

1. Kích hoạt môi trường ảo:
    ```bash
    .\venv\Scripts\Activate
    ```

2. Chạy ứng dụng:
    ```bash
    python app.py
    ```

3. Truy cập ứng dụng:
   - Mở trình duyệt web
   - Truy cập địa chỉ: `http://localhost:5000`
   - Tải lên hình ảnh và nhận kết quả nhận diện

## Huấn luyện mô hình

- Sử dụng file `Model_CNN_MobinetV2_Animals.ipynb` trên Google Colab (khuyến nghị)
- Hoặc chạy `model_cnn_mobinetv2_animals.py` trên máy local