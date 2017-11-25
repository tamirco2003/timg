from PIL import Image
import numpy as np
import sys

file_name = sys.argv[1] # Get file name.

imgArray = np.asarray(Image.open(file_name)) # Turn image into array.

imgArray = [[[hex(color)[2:] for color in pixel] for pixel in row] for row in imgArray] # Turn decimal ints into colors (hex).
imgArray = [[['0' + color if len(color) == 1 else color for color in pixel] for pixel in row] for row in imgArray] # Made sure all colors have 2 digits.
imgArray = [[''.join(pixel) for pixel in row] for row in imgArray] # Joined colors into pixels.
imgArray = [''.join(row) for row in imgArray] # Joined pixels into rows.
imgArray = '/'.join(imgArray) # Joined rows into string.

output = open("out.timg","w+") # Make a new timg file.
output.write(imgArray) # Write the picture into the timg file.
