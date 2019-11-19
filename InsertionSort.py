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


# Algorithm to implement insertion sort
def insertionSort(inputArray):
    # Traverse through 1 to len(inputArray)
    for i in range(1, len(inputArray)):

        # current element to be compared
        currentValue = inputArray[i]
        currentPosition = i - 1

        # compare the current element with the sorted portion and swapping
        while currentPosition >= 0 and currentValue < inputArray[currentPosition]:
            inputArray[currentPosition + 1] = inputArray[currentPosition]
            currentPosition -= 1

        # update the canvas frame after each comparison
        print(inputArray)
        animation()
        cv.delete(ALL)
        cv.update()

        inputArray[currentPosition + 1] = currentValue


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
insertionSort(randomData)
endTime = datetime.now()
print("Sorted list of size {} in {} seconds".format(len(randomData), endTime - startTime))

animation()
root.mainloop()