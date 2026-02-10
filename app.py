import numpy as np
import cv2
from PIL import Image
import tkinter as tk
from tkinter import filedialog
from image_display import ImageDisplay
from gui import ImageProcessorGUI

class ImageProcessor:
    def __init__(self, image_path):
        self.image_path = image_path
        self.image = cv2.imread(image_path)

    def process_image(self):
        # Convert the image to grayscale
        gray_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        # Apply a Gaussian blur to the image
        blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)
        # Perform edge detection using Canny
        edges = cv2.Canny(blurred_image, 50, 150)
        return edges
    
    def save_processed_image(self, output_path):
        edges = self.process_image()
        edges_pil = Image.fromarray(edges)
        edges_pil.save(output_path)

    def select_image():
        root = tk.Tk()
        root.withdraw()  # Hide the root window
        file_path = filedialog.askopenfilename(title="Select an image", filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
        return file_path
    
    def main(self):
        image_path = self.select_image()
        if image_path:
            self.save_processed_image('processed_image.png')
            print("Image processed and saved as 'processed_image.png'.")
        else:
            print("No image selected.")


    def process_image(image_path):
    # Load the image
        image = cv2.imread(image_path)
        # Convert the image to grayscale
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # Apply a Gaussian blur to the image
        blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)
        # Perform edge detection using Canny
        edges = cv2.Canny(blurred_image, 50, 150)
        # Convert edges to a PIL image and return
        edges_pil = Image.fromarray(edges)
        return edges_pil   



if __name__ == "__main__":
    # Example usage
    processor = ImageProcessor('input_image.jpg')
    processor.save_processed_image('processed_image.png') 