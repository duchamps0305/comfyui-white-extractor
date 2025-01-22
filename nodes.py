import cv2
import numpy as np
import torch

class WhitePercentage:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image": ("IMAGE",),
            },
        }

    RETURN_TYPES = ("FLOAT",)
    RETURN_NAMES = ("percentage",)
    FUNCTION = "calculate_white_percentage"
    CATEGORY = "Image Analysis"

    def calculate_white_percentage(self, image):
        # Convert the PyTorch tensor to a NumPy array
        img_np = (image[0].numpy() * 255).astype(np.uint8)

        # Convert to grayscale if the image is not already
        if len(img_np.shape) == 3 and img_np.shape[2] == 3:
            img_np = cv2.cvtColor(img_np, cv2.COLOR_RGB2GRAY)
        elif len(img_np.shape) == 3 and img_np.shape[2] == 4:
            # Handle RGBA images
            img_np = cv2.cvtColor(img_np, cv2.COLOR_RGBA2GRAY)

        # Convert to binary image
        _, binary_img = cv2.threshold(img_np, 254, 255, cv2.THRESH_BINARY)

        # Count the number of white pixels
        white_pixels = cv2.countNonZero(binary_img)

        # Calculate the total number of pixels
        total_pixels = binary_img.size

        # Calculate the percentage of white pixels
        white_percentage = (white_pixels / total_pixels) * 100

        # Limit to two decimal places
        white_percentage = round(white_percentage, 2)

        return (white_percentage,)

NODE_CLASS_MAPPINGS = {
    "WhitePercentage": WhitePercentage
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "WhitePercentage": "White Percentage"
}
