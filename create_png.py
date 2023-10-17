import os
import matplotlib.pyplot as plt


CURR_DIR_PATH = os.path.dirname(os.path.realpath(__file__))
# Load the image
diagram_image = plt.imread(CURR_DIR_PATH + '\\empty_sign.png')
plt.text(x=80, y=105, s="ABX 123", fontsize=70)
plt.imshow(diagram_image)
plt.show()
