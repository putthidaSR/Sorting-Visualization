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


# Utility method to sort elements in array in the correct order by placing any elements that are smaller than or equal to the pivot on the left side,
# and any elements that are greater than the pivot on the right side.
def partition(inputArray, start, end):
    i = j = start

    while j < end:
        if inputArray[j] <= inputArray[end]:
            inputArray[i], inputArray[j] = inputArray[j], inputArray[i]  # swap
            i += 1
        j += 1
    inputArray[i], inputArray[end] = inputArray[end], inputArray[i]  # place pivot element in its proper order
    return i


def quickSortRecursive(inputArray, start, end):
    # base case
    if start >= end:
        return  # done traversing array (elements are sorted)

    # partition the input array into two parts: less than pivot value and greater or equal to pivot value
    pivotLocation = partition(inputArray, start, end)

    quickSortRecursive(inputArray, start, pivotLocation - 1)  # sort elements before pivot
    quickSortRecursive(inputArray, pivotLocation + 1, end)  # sort elements after pivot

    print(inputArray)
    animation()
    cv.delete(ALL)
    cv.update()


def quicksort(inputArray):
    return quickSortRecursive(inputArray, 0, len(inputArray) - 1)


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
quicksort(randomData)
endTime = datetime.now()
print("Sorted list of size {} in {} seconds".format(len(randomData), endTime - startTime))

animation()
root.mainloop()