import streamlit as st

def page2_app():
    st.title("Technologies in Action 🧑‍💻")
    st.write("Welcome to the Technologie page! Here, we dive into the core technologies and methodologies driving our project.")
    
    # Data Processing Section
    st.header("Data Preprocessing 📊")
    st.write("""
    Before we can apply machine learning models to medical data, extensive data preprocessing is essential. This process includes 
    cleaning the data, normalizing it, and sometimes augmenting it to increase the dataset's robustness. Medical imaging data, such 
    as MRI scans, often need adjustments to ensure consistent quality and to highlight relevant features for analysis. By improving 
    the quality and reliability of input data, we enable our models to perform better in identifying brain tumors and other critical features.
    """)

    # CNN Section
    st.header("Convolutional Neural Networks (CNN) 🧠")
    st.write("""
    Convolutional Neural Networks (CNNs) are a foundational technology in our project, especially suited for image processing tasks. 
    CNNs are designed to recognize patterns in images by applying filters that detect features such as edges, textures, and shapes. 
    In the context of brain tumor detection, CNNs help analyze MRI scans by extracting spatial hierarchies in the data, allowing the model 
    to distinguish between normal and abnormal tissue structures. We have fine-tuned our CNN architecture to maximize accuracy 
    and minimize false positives and negatives.
    """)

    # YOLO Section
    st.header("YOLO (You Only Look Once) for Object Detection 🚀")
    st.write("""
    YOLO, or 'You Only Look Once', is a state-of-the-art object detection algorithm known for its speed and efficiency. YOLO divides 
    the input image into a grid, predicting bounding boxes and class probabilities for each section. For our project, YOLO enables 
    rapid identification and localization of brain tumors within MRI scans. Its single-pass architecture makes it much faster than 
    traditional methods, which is crucial for applications requiring real-time or near-real-time analysis. By utilizing YOLO, we ensure 
    that our model is both effective and efficient.
    """)

    # SAM2 YOLO Segmentation Section
    st.header("SAM2 YOLO for Image Segmentation 🧩")
    st.write("""
    SAM2 YOLO combines YOLO’s object detection strengths with advanced segmentation capabilities, allowing us to precisely segment 
    brain tumors. While YOLO identifies and classifies objects, SAM2 extends this by breaking down objects into detailed segments. 
    This is particularly useful in the medical field, where the exact boundaries of a tumor need to be identified for accurate diagnosis 
    and treatment planning. SAM2 YOLO provides pixel-level accuracy in delineating tumor regions, which is crucial for neurosurgeons 
    and oncologists who rely on precise imaging for surgical planning and radiotherapy targeting.
    """)

    # Summary
    st.write("""
    Together, these technologies create a powerful toolkit for brain tumor detection and segmentation. Our approach leverages the 
    strengths of CNNs, YOLO, and SAM2 YOLO to offer a comprehensive solution: from identifying anomalies in brain images to defining 
    precise tumor boundaries, enhancing the overall effectiveness of diagnosis and treatment.
    
    By implementing and fine-tuning these advanced machine learning models, we hope to support healthcare professionals in making 
    timely, accurate, and data-driven decisions for their patients.
    """)
