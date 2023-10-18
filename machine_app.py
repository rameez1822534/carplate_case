import os
from PIL import Image
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
import pickle
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report, confusion_matrix, ConfusionMatrixDisplay

CURR_DIR_PATH = os.path.dirname(os.path.realpath(__file__))
output_directory = (CURR_DIR_PATH + '\\registration_images')
all_images_df = pd.DataFrame()
images_processed = 0
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
        images_processed += 1
        print(images_processed)



#Devide data and labels into X and y
# y = all_images_df['Label']
# all_images_df.drop(['Label'], axis=1, inplace=True)
# X = all_images_df

y_test = all_images_df['Label']
all_images_df.drop(['Label'], axis=1, inplace=True)
X_test = all_images_df

#Train test split
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#train the model
pickle_directory = (CURR_DIR_PATH +"\\1000_model.pkl")
with open(pickle_directory, 'rb') as file:
    model = pickle.load(file)

# model = LogisticRegression()
# model.fit(X_train, y_train)

# Predict on the test set
y_pred = model.predict(X_test)

# Evaluate the model
print("Classification Report:")
print(classification_report(y_test, y_pred))

# Plot the confusion matrix
cm = confusion_matrix(y_test, y_pred)
cm_display = ConfusionMatrixDisplay(cm, display_labels=model.classes_).plot()
plt.show()

print("Model Classes:", model.classes_)
print("Unique Labels in y_test:", np.unique(y_test))

# Specify the path to save the model
filename = 'new_model.pkl'

# Open a file in write-binary mode and dump the model
with open(filename, 'wb') as file:
    pickle.dump(model, file)



