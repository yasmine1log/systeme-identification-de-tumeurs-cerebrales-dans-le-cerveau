# yolo1.py

import cv2
import numpy as np
import torch
from ultralytics import YOLO
from sam2.build_sam import build_sam2
from sam2.sam2_image_predictor import SAM2ImagePredictor
import supervision as sv
from PIL import Image

class YOLO_SAM_Detector:
    def __init__(self, yolo_model_path, sam_checkpoint_path, sam_config_path, device='cuda'):
        # Load YOLO model
        self.yolo_model = YOLO(yolo_model_path)
        self.device = torch.device(device if torch.cuda.is_available() else 'cpu')
        
        # Load SAM model
        self.sam_model = build_sam2(sam_config_path, sam_checkpoint_path, device=self.device, apply_postprocessing=False)
        self.predictor = SAM2ImagePredictor(self.sam_model)
    
    def detect_with_yolo(self, image):
        """Run YOLO detection on the input image."""
        results = self.yolo_model(image)
        return results
    
    def generate_sam_segmentation(self, image_rgb, boxes):
        """Generate segmentation mask using SAM based on YOLO-detected boxes."""
        self.predictor.set_image(image_rgb)
        masks, scores, logits = self.predictor.predict(box=boxes, multimask_output=False)
        return masks
    
    def process_image(self, image_path):
        """Process image with YOLO for detection, SAM for segmentation, and return annotated images."""
        # Load image
        image = cv2.imread(image_path)
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        
        # YOLO detection
        yolo_results = self.detect_with_yolo(image_rgb)
        boxes = yolo_results[0].boxes.xyxy.cpu().numpy()  # YOLO bounding boxes in [x_min, y_min, x_max, y_max]
        
        # SAM segmentation
        if len(boxes) > 0:
            masks = self.generate_sam_segmentation(image_rgb, boxes)
        else:
            raise ValueError("No detections found by YOLO model.")
        
        # Annotate detections and masks on the original image
        box_annotator = sv.BoxAnnotator(color_lookup=sv.ColorLookup.INDEX)
        mask_annotator = sv.MaskAnnotator(color_lookup=sv.ColorLookup.INDEX)
        
        detections = sv.Detections(xyxy=sv.mask_to_xyxy(masks=masks), mask=masks.astype(bool))
        detected_image = box_annotator.annotate(scene=image.copy(), detections=detections)
        segmented_image = mask_annotator.annotate(scene=image.copy(), detections=detections)
        
        # Extract isolated tumor
        isolated_tumor_image = self.isolate_tumor(image, masks)
        
        return detected_image, segmented_image, isolated_tumor_image
    
    def isolate_tumor(self, image, masks):
        """Create an isolated tumor image on a white background."""
        white_background = np.ones_like(image) * 255
        masks_binary = (masks > 0).astype(np.uint8)
        
        for i in range(masks_binary.shape[0]):
            mask = masks_binary[i]
            object_image = cv2.bitwise_and(image, image, mask=mask)
            
            # Find tumor bounding box
            x, y, w, h = cv2.boundingRect(mask)
            tumor_cropped = object_image[y:y+h, x:x+w]
            tumor_resized = cv2.resize(tumor_cropped, (white_background.shape[1], white_background.shape[0]), interpolation=cv2.INTER_CUBIC)
            tumor_resized[tumor_resized == 0] = 255  # Set black pixels to white
            
            return tumor_resized  # Single tumor extracted

# Example usage:
# detector = YOLO_SAM_Detector('path/to/yolo.pt', 'path/to/sam_checkpoint.pt', 'path/to/sam_config.yaml')
# detected_img, segmented_img, isolated_img = detector.process_image('path/to/image.jpg')
