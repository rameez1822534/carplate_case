from car_plate import create_plate
from create_png import generate_images_and_save #, find_files
import os

CURR_DIR_PATH = os.path.dirname(os.path.realpath(__file__))

for i in range(5):
    # Chose how many reg-numbers to create
    reg_list = create_plate(1)
    # chose directory for saving the pictures
    output_directory = (CURR_DIR_PATH + '\\registration_images')
    # Create images and save in folder
    generate_images_and_save(reg_list, output_directory)
    print("Image", i," created")



# Count how many files we have
# find_files('.png',output_directory)
