import sys
import time
import random

from datetime import datetime
from Constants import *

# Utilize Tkinter library to generate graph animation
if sys.version_info[0] == 3:
    from tkinter import *  # Python v.3+
else:
    from Tkinter import *  # Python v.2+


# Algorithm to implement selection sort
def selectionSort(inputArray):
    # Traverse through all lstay elements
    for i in range(len(inputArray)):

        # loop through every other element in the list to find the smallest one
        minIndex = i
        for j in range(i + 1, len(inputArray)):
            if inputArray[minIndex] > inputArray[j]:
                minIndex = j

                # swap the current element with the smallest element found
        inputArray[i], inputArray[minIndex] = inputArray[minIndex], inputArray[i]

        # update the canvas frame after each swap
        print(inputArray)
        animation()
        cv.delete(ALL)
        cv.update()


def animation():
    startingPositionX = 100  # starting position on x-axis of the first bar
    startingPositionY = 700  # bottom left of the first bar

    for item in randomData:
        cv.delete([item])
        bar = cv.create_rectangle(startingPositionX, startingPositionY, startingPositionX + barWidth,
                                  startingPositionY - (item * barWidth), fill=barColor)
        startingPositionX += barWidth + barSpace
        time.sleep(pauseTime)
        cv.update()


# Canvas
root = Tk()
root.title(title)
cv = Canvas(width=canvasWidth, height=canvasHeight, bg=backgroundColor)
cv.pack()
cv.update()

# Record runtime of the algorithm based on the provided input array
startTime = datetime.now()
selectionSort(randomData)
endTime = datetime.now()
print("Sorted list of size {} in {} seconds".format(len(randomData), endTime - startTime))

animation()
root.mainloop()