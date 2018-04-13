from PIL import Image
import numpy as np
import sys
import binascii

file_name = sys.argv[1] # Get file name.

imgArray = np.asarray(Image.open(file_name).convert('RGBA')) # Turn image into array.\

imgArray = [[[hex(color)[2:] for color in pixel] for pixel in row] for row in imgArray] # Turn decimal ints into colors (hex).
imgArray = [[['0' + color if len(color) == 1 else color for color in pixel] for pixel in row] for row in imgArray] # Made sure all colors have 2 digits.
imgArray = [[''.join(pixel) for pixel in row] for row in imgArray] # Joined colors into pixels.
imgArray = [''.join(row) for row in imgArray] # Joined pixels into rows.
numOfRow = '0' + hex(len(imgArray))[2:] if len(hex(len(imgArray))[2:]) % 2 == 1 else hex(len(imgArray))[2:] # Add 0 to each 1 digit byte.
lenOfNumOfRow = '0' + hex(int(len(numOfRow) / 2))[2:] if len(hex(int(len(numOfRow) / 2))[2:]) % 2 == 1 else hex(int(len(numOfRow) / 2))[2:] # Add 0 to each 1 digit byte.
imgArray = lenOfNumOfRow + numOfRow + ''.join(imgArray) # Joined rows into string.

output = open("out.timg","wb") # Make a new timg file.
output.write(binascii.unhexlify(imgArray)) # Write the picture into the timg file.
