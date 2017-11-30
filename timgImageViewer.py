import re
import PIL.Image
import PIL.ImageTk
import numpy as np
import sys
from tkinter import *

# Function to get each byte.
def bytes_from_file(filename, chunksize=8192):
    with open(filename, "rb") as f:
        while True:
            chunk = f.read(chunksize)
            if chunk:
                for b in chunk:
                    yield b
            else:
                break

# Function to devide array into equal parts.
devideIntoEqualParts = lambda lst, sz: [lst[i:i+sz] for i in range(0, len(lst), sz)]

file_name = sys.argv[1] # Get file name.
timg = [] # Create new array for all bytes.

# Add all bytes to array
for b in bytes_from_file(file_name):
    timg.append(hex(b)[2:])

lenOfNumOfRow = int(timg[0], 16) # Get number of bytes of number of lines.
del timg[0] # Delete it from the array.
numOfRow = "" # Create new string for number of lines in hex.

for x in range(0, lenOfNumOfRow):
    numOfRow += timg[0] # Add hex of number of lines.
    del timg[0] # Delete bytes of number of lines from array.

numOfRow = int(numOfRow, 16) # Make number of lines an integer.
timg = devideIntoEqualParts(timg, int(len(timg) / numOfRow)) # Devide file into rows.
timg = [devideIntoEqualParts(row, 3) for row in timg] # Devide rows into pixels.
timg = [[[np.uint8(int(color, 16)) for color in pixel] for pixel in row] for row in timg] # Make all colors uint8.
timg = np.asarray(timg) # Turn list into array.

root = Tk()

timgImg = PIL.ImageTk.PhotoImage(PIL.Image.fromarray(timg))
label = Label(root, image = timgImg)
label.grid(row = 0)

root.mainloop()
