import matplotlib.pyplot as plt
import os


banned_words = ['APA','ARG','ASS','BAJ','BSS','CUC','CUK','DUM','ETA','ETT','FAG','FAN','FEG','FEL','FEM','FES',\
                'FET','FNL','FUC','FUK','FUL','GAM','GAY','GEJ','GEY','GHB','GUD','GYN','HAT','HBT','HKH','HOR',\
                'HOT','KGB','KKK','KUC','KUF','KUG','KUK','KYK','LAM','LAT','LEM','LOJ','LSD','LUS','MAD','MAO',\
                'MEN','MES','MLB','MUS','NAZ','NRP','NSF','NYP','OND','OOO','ORM','PAJ','PKK','PLO','PMS','PUB',\
                'RAP','RAS','ROM','RPS','RUS','SEG','SEX','SJU','SOS','SPY','SUG','SUP','SUR','TBC','TOA','TOK',\
                'TRE','TYP','UFO','USA','WAM','WAR','WWW','XTC','XTZ','XXL','XXX','ZEX','ZOG','ZPY','ZUG','ZUP','ZOO']

banned_letters = ['I','Q','V','Å','Ä', 'Ö']

CURR_DIR_PATH = os.path.dirname(os.path.realpath(__file__))
# Load the image
diagram_image = plt.imread(CURR_DIR_PATH + '\\empty_sign.png')
plt.text(x=80, y=105, s="ABX 123", fontsize=70)
plt.imshow(diagram_image)
plt.show()

