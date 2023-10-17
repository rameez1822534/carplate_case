import os
from PIL import Image
import numpy as np
import pandas as pd

CURR_DIR_PATH = os.path.dirname(os.path.realpath(__file__))
output_directory = (CURR_DIR_PATH + '\\registration_images')
all_images_df = pd.DataFrame()
for root, _, files in os.walk(output_directory):
    for filename in files:
        file_path = os.path.join(root, filename)
        # Open the image
        image = Image.open(file_path)
        # Define the coordinates of the region you want to crop (left, upper, right, lower)
        crop_box = (145, 210, 205, 280)  # Example coordinates, adjust them as needed

        # Crop the region from the image
        cropped_image = image.crop(crop_box)
        # cropped_image.show()
        # Create an array and save a dataframe
        image = np.array(cropped_image)
        image2 = image.flatten()

        df = pd.DataFrame([image2])
        # Add label
        df['Label'] = root[-1]
        all_images_df = all_images_df.append(df, ignore_index=True)