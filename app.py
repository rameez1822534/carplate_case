from car_plate import create_plate
from create_png import generate_images_and_save, find_files
import os

CURR_DIR_PATH = os.path.dirname(os.path.realpath(__file__))

reg_list = create_plate(1)
output_directory = (CURR_DIR_PATH + '\\registration_images')
generate_images_and_save(reg_list, output_directory)

find_files('.png',output_directory)
