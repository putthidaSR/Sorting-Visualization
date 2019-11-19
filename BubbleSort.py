import sys
import time
import random

from datetime import datetime
from Constants import *

# Utilize Tkinter library to generate graph animation
if sys.version_info[0] == 3:
    from tkinter import * # Python v.3+
else:
    from Tkinter import * # Python v.2+

# Algorithm to implement bubble sort
def bubbleSort(inputArray):

    # Traverse through all elements in the given inputArrayay
    for number in range(len(inputArray)-1, 0, -1):
        for i in range(number):

            # swap each pair of adjacent elements if they are not in order
            if inputArray[i] > inputArray[i + 1]:
                inputArray[i], inputArray[i + 1] = inputArray[i + 1], inputArray[i]

                print(inputArray)

                # draw a frame on canvas after each swap
                animation()
                cv.delete(ALL)
                cv.update()

def animation():

    startingPositionX = 100 # starting position on x-axis of the first bar
    startingPositionY = 700 # bottom left of the first bar

    for item in randomData:
        cv.delete([item])
        bar = cv.create_rectangle(startingPositionX, startingPositionY, startingPositionX + barWidth, startingPositionY - (item * barWidth), fill = barColor)
        startingPositionX += barWidth + barSpace
        time.sleep(pauseTime)
        cv.update()

#Canvas
root = Tk()
root.title(title)
cv = Canvas(width = canvasWidth, height = canvasHeight, bg = backgroundColor)
cv.pack()
cv.update()

# Record runtime of the algorithm based on the provided input array
startTime = datetime.now()
bubbleSort(randomData)
endTime = datetime.now()
print("Sorted list of size {} in {} seconds".format(len(randomData), endTime - startTime))

animation()
root.mainloop()