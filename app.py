import os
import numpy as np
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from PIL import Image

# Khởi tạo Flask app
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'

# Load mô hình đã huấn luyện
model_path = os.path.join(os.path.dirname(__file__), 'animal_classification_mobilenetv2.h5')
model = load_model(model_path)
IMG_WIDTH, IMG_HEIGHT = 224, 224

# Danh sách lớp
CLASS_NAMES = [
    'dog', 'horse', 'elephant', 
    'butterfly', 'chicken', 'cat', 
    'cow', 'sheep','spider', 'squirrel',
]

# Hàm xử lý ảnh và dự đoán
def predict_image(file_path):
    img = Image.open(file_path).convert('RGB')
    img = img.resize((IMG_WIDTH, IMG_HEIGHT))
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    prediction = model.predict(img_array)
    predicted_class = CLASS_NAMES[np.argmax(prediction)]
    confidence = np.max(prediction) * 100
    return predicted_class, confidence

# Trang chính
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'image' not in request.files:
            return render_template(
                'index.html', 
                error='Không tìm thấy file ảnh!'
            )

        file = request.files['image']
        if file.filename == '':
            return render_template(
                'index.html', 
                error='Vui lòng chọn một file ảnh!'
            )    

        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        predicted_class, confidence = predict_image(file_path)

        return render_template(
            'index.html',
            prediction=predicted_class,
            confidence=f"{confidence:.2f}%",
            image_url=file_path
        )

    return render_template('index.html')

# Chạy ứng dụng
if __name__ == '__main__':
    app.run(debug=True)
