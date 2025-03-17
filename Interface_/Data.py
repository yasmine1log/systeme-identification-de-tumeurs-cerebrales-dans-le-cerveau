import os
import subprocess
from sqlalchemy import create_engine, Column, Integer, String #type:ignore 
from sqlalchemy.ext.declarative import declarative_base #type:ignore 






from sqlalchemy.orm import sessionmaker #type:ignore 

# Paths and thresholds
DATABASE_PATH = 'sqlite:///image_db.sqlite'
IMAGE_FOLDER = 'images'
SCRIPT_PATHS = ['cnn.py', 'yolo1.py', 'yolo2.py', 'sam.py']
IMAGE_THRESHOLD = 100

# Initialize the database connection and session
engine = create_engine(DATABASE_PATH)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

# Define the ImageEntry model for tracking images in the database
class ImageEntry(Base):
    __tablename__ = 'images'
    id = Column(Integer, primary_key=True)
    filename = Column(String, nullable=False)

# Create the images table if it doesn't exist
Base.metadata.create_all(engine)

# Ensure the image folder exists
if not os.path.exists(IMAGE_FOLDER):
    os.makedirs(IMAGE_FOLDER)

# Function to add an image to the database and folder
def insert_image(image_data, filename):
    # Save the image to the designated folder
    image_path = os.path.join(IMAGE_FOLDER, filename)
    with open(image_path, 'wb') as f:
        f.write(image_data)

    # Add image entry to the database
    new_image = ImageEntry(filename=filename)
    session.add(new_image)
    session.commit()

    # Check if the number of images has reached the threshold
    if session.query(ImageEntry).count() >= IMAGE_THRESHOLD:
        trigger_scripts()

# Function to run external Python scripts
def trigger_scripts():
    print("Threshold reached! Running scripts...")
    # Run each script in the specified order
    for script in SCRIPT_PATHS:
        try:
            subprocess.run(['python', script], check=True)
            print(f"Executed {script} successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Error running {script}: {e}")

    # Clear the database to reset the count after reaching the threshold
    session.query(ImageEntry).delete()
    session.commit()
    print("Database cleared for next batch.")

# Example usage of inserting images
def main():
    # Insert an image into the system
    # Replace 'sample_image.jpg' with the actual image file
    with open("sample_image.jpg", "rb") as img_file:
        image_data = img_file.read()
        insert_image(image_data, "sample_image.jpg")

if __name__ == "__main__":
    main()

# cnn.py
print("Running CNN script...")

# yolo1.py
print("Running YOLO1 script...")

# yolo2.py
print("Running YOLO2 script...")

# sam.py
print("Running SAM script...")
