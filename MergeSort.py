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

# Implementation of merge sort algorithm
def mergeSort(inputArray):

    if len(inputArray) > 1:
        mid = len(inputArray) // 2
        leftSlot = inputArray[:mid]
        rightSlot = inputArray[mid:]

        # Sort left and right half
        mergeSort(leftSlot)
        mergeSort(rightSlot)

        i=0
        j=0
        k=0

        # Iterate over left and right slots of the input array and store it into the temporary array as a place holder
        while i < len(leftSlot) and j < len(rightSlot):
            if leftSlot[i] <= rightSlot[j]:
                inputArray[k]=leftSlot[i]
                i += 1
            else:
                inputArray[k] = rightSlot[j]
                j += 1
            k += 1

        #When reaching here, that means the above loop has completed. So both the right and the left side of the sub-array can be considered sorted.
        while i < len(leftSlot):
            inputArray[k] = leftSlot[i]
            i += 1
            k += 1

        while j < len(rightSlot):
            inputArray[k] = rightSlot[j]
            j += 1
            k += 1

    print(inputArray)
    animation()
    cv.delete(ALL)
    cv.update()

def animation():

    startingPositionX = 100 # starting position on x-axis of the first bar
    startingPositionY = 700 # bottom left of the first bar

    for item in almostSortedData:
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
mergeSort(almostSortedData)
endTime = datetime.now()
print("Sorted list of size {} in {} seconds".format(len(almostSortedData), endTime - startTime))

animation()
root.mainloop()