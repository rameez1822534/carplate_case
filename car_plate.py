# Function to generate regisration plates

import random
import string

def create_plate():
    banned_words = ['APA','ARG','ASS','BAJ','BSS','CUC','CUK','DUM','ETA','ETT','FAG','FAN','FEG','FEL','FEM','FES', 'FET', 'FNL']
    # copy in from Peter's slides

    random_string = ""
    random_numbers = ""

    while len(random_string) < 3:
        letter = str(random.choice(string.ascii_letters))
        letter = letter.upper()
        if letter == 'I' or letter == 'V' or letter == 'Q':
            pass
        else:
            random_string = random_string + letter
            # random_string = 'APA'
        if random_string in banned_words:
            random_string = ""
            # print("Banned word!")


    for number in range(3):
        numbers = str(random.randint(0,9))
        random_numbers = random_numbers + numbers

    random_plate = random_string + " " + random_numbers

    return random_plate

# plate1 = create_plate()
# print(plate1)

