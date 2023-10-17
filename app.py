from car_plate import create_plate
from create_png import generate_images_and_save
import os

CURR_DIR_PATH = os.path.dirname(os.path.realpath(__file__))

reg_list = create_plate(3)
output_directory = (CURR_DIR_PATH + '\\registration_images')
generate_images_and_save(reg_list, output_directory)

file_type = '.png'

def find_files(file_type, directory):
    """Use filetype to count files in a folder and its subfolders."""
    file_count = 0
    for root, _, files in os.walk(directory):
        for filename in files:
            if filename.lower().endswith(file_type):
                file_count += 1

    if file_count >= 1:
        print(f"The folder and its subfolders have {file_count} {file_type} files")
    else:
        print(f"There are no {file_type} files in this folder and its subfolders")

find_files(file_type, output_directory)
