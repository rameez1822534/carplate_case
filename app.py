from car_plate import create_plate
from create_png import generate_images_and_save
import os
CURR_DIR_PATH = os.path.dirname(os.path.realpath(__file__))

# def create_plate(nr_of_plates):
#     list_of_plates = []
#     for plates in nr_of_plates:
#         list_of_plates.append(plate)
    
#     return list_of_plates #list of strings "ABC 123"

# def create_licence_plates():    
#     pass

create_plate(2)
output_directory = (CURR_DIR_PATH + '\\registration_images')
generate_images_and_save(output_directory)