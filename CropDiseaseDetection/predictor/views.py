from django.shortcuts import render
from django.core.files.storage import default_storage
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os
from django.core.files.storage import default_storage


# Load the trained model
model_path = os.path.join(os.path.dirname(__file__), 'model1.h5')  # Adjust path if needed
model = load_model(model_path)

# Define the expected image size
IMG_HEIGHT, IMG_WIDTH = 256, 256  # Make sure this matches your trained model

# Define class labels (Update with your dataset's class labels)
class_labels = [
    "Bacterial Spot", "Early Blight", "Late Blight", "Leaf Mold", "Septoria Leaf Spot",
    "Spider Mites", "Target Spot", "Yellow Leaf Curl Virus", "Mosaic Virus", "Healthy"
]

def predict_disease(request):
    if request.method == 'POST' and request.FILES.get('image'):
        img_file = request.FILES['image']
        file_path = default_storage.save('temp/' + img_file.name, img_file)
        file_path = default_storage.path(file_path)

        img = image.load_img(file_path, target_size=(256, 256))
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0) / 255.0

        predictions = model.predict(img_array)
        predicted_class_index = np.argmax(predictions)
        confidence_scores = predictions[0].tolist()

        predicted_disease = class_labels[predicted_class_index]
        confidence = np.max(predictions)

        default_storage.delete(file_path)

        return render(request, 'result.html', {
            'disease': predicted_disease,
            'confidence': f"{confidence * 100:.2f}%",
            'confidence_scores': confidence_scores,
            'class_labels': class_labels
        })

    return render(request, 'index.html')



