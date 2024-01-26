import cv2
import numpy as np

def detect_corners(image_path):
    # Read the image
    img = cv2.imread(image_path)
    
    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Detect corners using Harris Corner Detection
    corners = cv2.cornerHarris(gray, blockSize=2, ksize=3, k=0.04)
    
    # Threshold for an optimal value, it may vary depending on the image
    threshold = 0.01 * corners.max()
    
    # Mark the corners on the image
    img[corners > threshold] = [0, 0, 255]  # Red color for corners
    
    # Display the result
    cv2.imshow('Corners Detected', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Specify the path to your image
image_path = 'm2.jpg'

# Call the function to detect corners
detect_corners(image_path)
