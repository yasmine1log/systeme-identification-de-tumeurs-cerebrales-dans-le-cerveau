# yolo2_segmentation.py

from ultralytics import YOLO
from PIL import Image

# Load the YOLOv8 segmentation model
model_path = "path/to/your/yolo2.pt"  # Replace with the actual path to your segmentation model
model = YOLO(model_path)  # Load YOLOv8 model for segmentation

# Function to run segmentation on an image
def segment_objects(image_path):
    results = model(image_path, task='segment')  # Specify task as 'segment' for segmentation
    return results

# Function to display results
def display_segmentation_results(results):
    results[0].plot()  # Plots and displays the image with segmented masks and labels

# Example usage
if __name__ == "__main__":
    image_path = "path/to/test_image.jpg"  # Replace with the path to an image for testing
    results = segment_objects(image_path)
    display_segmentation_results(results)
