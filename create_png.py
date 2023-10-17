import os
import matplotlib.pyplot as plt


CURR_DIR_PATH = os.path.dirname(os.path.realpath(__file__))


reg_list = ['APA 123','BAJ 554','BSS 532','FUK 065','CUK 275','SEX 923','FAN 368','PAJ 960','GAM 9311','GYN','HAT',\
            'ZUP 612','HKH','TYP 023','UFO 532','USA 064','WAM 853','XTC','XTZ 041','ZEX','KKK 638','ZUG','ZOO']

def generate_images_and_save(characters_list, output_directory):
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    for random_plate in characters_list:
        # Get the first character to determine the folder name
        first_character = random_plate[0]

        # Create a folder for the category if it doesn't exist
        category_directory = os.path.join(output_directory, first_character)
        if not os.path.exists(category_directory):
            os.makedirs(category_directory)

        for _ in range(len(characters_list)):
            # Create an image with the registration plate
            plate_image = plt.imread(CURR_DIR_PATH + '\\empty_sign.png')
            plt.text(x=80, y=105, s=random_plate, fontsize=64, horizontalalignment='left', fontname='Courier New')

            # Save the image to the category folder
            image_filename = f"{random_plate}.png"
            image_path = os.path.join(category_directory, image_filename)
            plt.imshow(plate_image)
            plt.savefig(image_path)
            plt.close()


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




if __name__ == "__main__":
    # Example usage:
    characters_list = reg_list
    output_directory = (CURR_DIR_PATH + '\\registration_images')

    generate_images_and_save(characters_list, output_directory)
    find_files(file_type, output_directory)
    print("Images generated and saved.")