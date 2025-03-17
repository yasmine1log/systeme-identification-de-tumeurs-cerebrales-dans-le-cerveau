# page4.py

import streamlit as st
from yolo1 import YOLO_SAM_Detector
from PIL import Image
import numpy as np
import tempfile

def page4_app():
    # Set up the page title and instructions
    st.markdown("""
        <style>
            .centered-content {
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                text-align: center;
            }
            .centered-content img {
                margin: auto;
            }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("<div class='centered-content'><h1>🧪 Analysis Page - Tumor Detection & Segmentation</h1></div>", unsafe_allow_html=True)
    st.markdown("<div class='centered-content'><p>Upload an MRI image to detect and segment brain tumors.</p></div>", unsafe_allow_html=True)

    # Initialize the YOLO_SAM_Detector with paths to models
    yolo_model_path = r"C:\Users\hp\Downloads\yolo.pt"  # Using raw string for Windows path
    sam_checkpoint_path = r"C:\Users\hp\Downloads\sam2_hiera_large.pt"
    sam_config_path = r"C:\Users\hp\Downloads\sam2_hiera_l.yaml"
    detector = YOLO_SAM_Detector(yolo_model_path, sam_checkpoint_path, sam_config_path)

    # Image upload
    uploaded_file = st.file_uploader("Choose an MRI image...", type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        # Save and load the uploaded image
        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            tmp.write(uploaded_file.read())
            image_path = tmp.name

        # Display the uploaded image at a larger size (550) and centered
        st.markdown("<div class='centered-content'><h3>🖼️ Uploaded Image</h3></div>", unsafe_allow_html=True)
        image = Image.open(image_path)
        st.markdown("<div class='centered-content'>", unsafe_allow_html=True)
        st.image(image, caption="Uploaded MRI Image", width=550)
        st.markdown("</div>", unsafe_allow_html=True)

        # Run detection and segmentation
        try:
            detected_img, segmented_img, isolated_img = detector.process_image(image_path)
            
            # Display the YOLO detection result at a larger size (550) and centered
            st.markdown("<div class='centered-content'><h3>📊 YOLO Detection Result</h3></div>", unsafe_allow_html=True)
            st.markdown("<div class='centered-content'>", unsafe_allow_html=True)
            st.image(detected_img, caption="YOLO Detection with Bounding Boxes", width=550)
            st.markdown("</div>", unsafe_allow_html=True)
            
            # Display the SAM segmentation result at a larger size (550) and centered
            st.markdown("<div class='centered-content'><h3>🔍 SAM Segmentation Result</h3></div>", unsafe_allow_html=True)
            st.markdown("<div class='centered-content'>", unsafe_allow_html=True)
            st.image(segmented_img, caption="SAM Segmentation Mask Overlay", width=550)
            st.markdown("</div>", unsafe_allow_html=True)
            
            # Display the isolated tumor image at a larger size (550) and centered
            st.markdown("<div class='centered-content'><h3>🧠 Isolated Tumor Image</h3></div>", unsafe_allow_html=True)
            st.markdown("<div class='centered-content'>", unsafe_allow_html=True)
            st.image(isolated_img, caption="Isolated Tumor on White Background", width=550)
            st.markdown("</div>", unsafe_allow_html=True)
        
        except Exception as e:
            st.error(f"An error occurred during processing: {str(e)}")

# Ensure the function is accessible to app.py
