import re
from PIL import Image
import numpy as np
import sys

file_name = sys.argv[1] # Get file name.

timg = open(file_name, "r") # Read file.
strTimg = str(timg.read()) # Make file into string.
strTimg = strTimg.split('/') # Split string into rows.
strTimg = [re.findall('......', row) for row in strTimg] # Split rows into pixels.
strTimg = [[re.findall('..', pixel) for pixel in row] for row in strTimg] # Split pixels into colors.
strTimg = [[[np.uint8(int(color, 16)) for color in pixel] for pixel in row] for row in strTimg] # Change colors into decimal ints, then into uint8s.
strTimg = np.asarray(strTimg) # Change the list into a numpy array.

Image.fromarray(strTimg).save('out.png')