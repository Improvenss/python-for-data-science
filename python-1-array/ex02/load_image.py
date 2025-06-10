#!/usr/bin/env python3.10
# Allowed functions : all libs for load images and table manipulation

from typing import Union
import numpy as np
from PIL import Image
import os

# def ft_load(path: str) -> array:
#     print("asdf")

    # load_image.py

def ft_load(path: str) -> Union[np.ndarray, None]:
    """
    Loads an image and returns its content as an RGB array.
    Prints image shape and format.
    """
    if not isinstance(path, str):
        print("Error: path must be a string.")
        return None

    if not os.path.isfile(path):
        print(f"Error: File not found: '{path}'")
        return None

    try:
        with Image.open(path) as img:
            if img.format not in ("JPEG", "JPG"):
                print("Error: Only JPEG/JPG images are supported.")
                return None

            img_rgb = img.convert("RGB")
            img_array = np.array(img_rgb)
            print(f"The shape of image is: {img_array.shape}")
            return img_array

    except Exception as e:
        print(f"Error loading image: {e}")
        return None