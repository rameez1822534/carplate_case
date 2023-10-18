import os
from PIL import Image
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

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
        all_images_df = pd.concat([all_images_df, df], ignore_index=True)
        
y = all_images_df['Label']
all_images_df.drop(['Label'], axis=1, inplace=True)
X = all_images_df
# Take out training data
X_train, X_test,y_train, y_test = train_test_split(
    X, y, test_size=0.2)
# Create model
model = LinearRegression()
model.fit(X_train,y_train)
# create a predictions 
y_predict = model.predict(X_test)






