# Function to generate regisration plates

import random
import string

def create_plate(number_of_plates_to_create):
    list_of_created_plates = []
    banned_words = ['APA','ARG','ASS','BAJ','BSS','CUC','CUK','DUM','ETA','ETT','FAG','FAN','FEG','FEL','FEM','FES',\
                'FET','FNL','FUC','FUK','FUL','GAM','GAY','GEJ','GEY','GHB','GUD','GYN','HAT','HBT','HKH','HOR',\
                'HOT','KGB','KKK','KUC','KUF','KUG','KUK','KYK','LAM','LAT','LEM','LOJ','LSD','LUS','MAD','MAO',\
                'MEN','MES','MLB','MUS','NAZ','NRP','NSF','NYP','OND','OOO','ORM','PAJ','PKK','PLO','PMS','PUB',\
                'RAP','RAS','ROM','RPS','RUS','SEG','SEX','SJU','SOS','SPY','SUG','SUP','SUR','TBC','TOA','TOK',\
                'TRE','TYP','UFO','USA','WAM','WAR','WWW','XTC','XTZ','XXL','XXX','ZEX','ZOG','ZPY','ZUG','ZUP','ZOO']
    # copy in from Peter's slides
    for i in range(number_of_plates_to_create):
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
        list_of_created_plates.append(random_plate)

    return list_of_created_plates

# plate1 = create_plate()
# print(plate1)

if __name__ == "__main__":
    x = create_plate(20)
    print(x)

