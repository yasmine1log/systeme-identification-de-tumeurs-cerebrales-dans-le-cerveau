# cnn.py

import tensorflow as tf
from tensorflow.keras.models import load_model # type: ignore
from tensorflow.keras.preprocessing.image import img_to_array # type: ignore
from PIL import Image
import numpy as np

# Load the trained model
model_path = "path/to/your/cnn_model.h5"  # Replace with your actual model path
model = load_model(model_path)

# Define image transformation
def preprocess_image(image_path):
    image = Image.open(image_path).convert('RGB')
    image = image.resize((512, 512))  # Resize to 512x512
    image = img_to_array(image) / 255.0  # Scale pixel values
    image = np.expand_dims(image, axis=0)  # Add batch dimension
    return image

# Function to classify an image
def classify_image(image_path):
    image = preprocess_image(image_path)
    prediction = model.predict(image)
    predicted_class = np.argmax(prediction, axis=1)[0]
    return predicted_class
