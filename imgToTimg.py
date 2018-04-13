from PIL import Image
import numpy as np
import sys
import binascii

file_name = sys.argv[1] # Get file name.

imgArray = np.asarray(Image.open(file_name).convert('RGBA')) # Turn image into array.

def colorToHex(color):
    hexColor = hex(color)[2:] # Turn decimal ints into colors (hex).
    if (len(hexColor) < 2):
        hexColor = '0' + hexColor # Made sure all colors have 2 digits.
    return hexColor

def joinArray(array):
    array = [[''.join(pixel) for pixel in row] for row in array] # Joined colors into pixels.
    array = [''.join(row) for row in array] # Joined pixels into rows.
    return array

def addZero(string):
    if (len(string) % 2 != 0):
        return '0' + string
    else:
        return string

imgArray = [[[colorToHex(color) for color in pixel] for pixel in row] for row in imgArray]
imgArray = joinArray(imgArray)
numOfRow = addZero(hex(len(imgArray))[2:])
lenOfNumOfRow = addZero(hex(int(len(numOfRow) / 2))[2:])
imgArray = lenOfNumOfRow + numOfRow + ''.join(imgArray) # Joined rows into string.

output = open("out.timg","wb") # Make a new timg file.
output.write(binascii.unhexlify(imgArray)) # Write the picture into the timg file.
