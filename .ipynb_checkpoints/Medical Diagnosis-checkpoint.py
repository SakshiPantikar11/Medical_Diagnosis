import os
from kaggle.api.kaggle_api_extended import KaggleApi

# Initialize Kaggle API
api = KaggleApi()
api.authenticate()

# Download the dataset
dataset_name = "nodoubttome/skin-cancer9-classesisic"
dataset_path = "skin_cancer_dataset"  # You can change the path here

# Download the dataset
api.dataset_download_files(dataset_name, path=dataset_path, unzip=True)

print(f"Dataset downloaded to {dataset_path}")

import kagglehub

# Download latest version
path = kagglehub.dataset_download("nodoubttome/skin-cancer9-classesisic")

print("Path to dataset files:", path)

import cv2
import numpy as np
import os

# Path to the dataset folder
dataset_path = 'skin_cancer_dataset'  # Change if necessary
import time
from kaggle.api.kaggle_api_extended import KaggleApi
from urllib3.exceptions import IncompleteRead
import requests

api = KaggleApi()
api.authenticate()

dataset_name = 'nodoubttome/skin-cancer9-classesisic'
dataset_path = 'path_to_your_download_location'


def download_with_retry():
    retries = 3  # Retry 3 times
    for attempt in range(retries):
        try:
            api.dataset_download_files(dataset_name, path=dataset_path, unzip=True)
            print("Dataset downloaded successfully.")
            break  # Exit if download is successful
        except (IncompleteRead, requests.exceptions.RequestException) as e:
            print(f"Error during download (attempt {attempt + 1}/{retries}): {e}")
            time.sleep(5)  # Wait before retrying
        if attempt == retries - 1:
            print("Max retries reached. Download failed.")


download_with_retry()


# Rest of your code

# Function to load and   preprocess the images
def load_images_from_folder(folder, img_size=(224, 224)):
    images = []
    labels = []
    class_names = os.listdir(folder)
    for label, class_name in enumerate(class_names):
        class_folder = os.path.join(folder, class_name)
        if os.path.isdir(class_folder):
            for filename in os.listdir(class_folder):
                img_path = os.path.join(class_folder, filename)
                valid_extensions = ['.jpg', '.jpeg', '.png', '.bmp', '.tiff']
                if filename.lower().endswith(tuple(valid_extensions)):
                    img = cv2.imread(img_path)
                    img = cv2.resize(img, img_size)
                    img = img / 255.0  # Normalize the image to [0, 1]
                    images.append(img)
                    labels.append(label)
    return np.array(images), np.array(labels)

print(f"Number of images: {len(X)}")
print(f"Number of labels: {len(y)}")

# Load images and labels
X, y = load_images_from_folder(dataset_path)
print(f"Loaded {len(X)} images")

from sklearn.model_selection import train_test_split

# Split the dataset into training and validation sets
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

print(f"Training data: {len(X_train)} images")
print(f"Validation data: {len(X_val)} images")