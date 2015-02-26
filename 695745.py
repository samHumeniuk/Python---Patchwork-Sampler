#UP695745
#Python Coursewok - A PatchWork Sampler


# Global constants
width = 100
height = 100
margin = 2
padding = -1


#Lists:
patchTypeList = []
coloursList = []


import math
from graphics import *
from math import floor

def main():
#Ask user for sizes
    #numberAcross = getInt("width")
    #numberUp = getInt("height")
    numberAcross = getInt("size")
    numberUp = numberAcross
#Ask the user for Colours
    colourOne, colourTwo, colourThree = askForColours()
#Draw graphics window
    windowWidth = width * numberAcross + padding
    windowHeight = height * numberUp + padding
    patchWindow = GraphWin("Patchwork Sampler", windowWidth, windowHeight)
#Draw Patchwork
    drawPatchwork(patchWindow, numberAcross, numberUp, colourOne, colourTwo, colourThree)
#Allow user to over two swap patches
    allowSwappingPatches(patchWindow, numberAcross, colourOne, colourTwo, colourThree)


#Asks the user for either the height or the width until valid value is entered
def getInt(variableName):
    value = "0"
    minValue = 2
    maxvalue = 9
    while value.isdigit() == False or not( minValue <= int(value) <= maxvalue):
        promt = "Please enter the " + variableName \
        + " of the Patchwork (must be a whole number between " \
        + str(minValue) + " and " + str(maxvalue) + ")"
        value = str(input(promt))
    return int(value)

#Asks the user for three different, valid colours
def askForColours():
    colourOne = getColour("first colour")
    colourTwo = getColour("second colour")
    colourTwo, changesMade = checkNotSameColours(colourOne, colourTwo,)
    colourThree = getColour("third colour")
    changesMadeone = True
    changesMadetwo = True
    while changesMadeone == True or changesMadetwo == True:
        colourThree, changesMadeone = checkNotSameColours(colourOne, colourThree)
        colourThree, changesMadetwo = checkNotSameColours(colourTwo, colourThree)
    return colourOne, colourTwo, colourThree

#Asks the user for a colour and checks it's valid.
def getColour(colourNumber):
    promt = "Please enter the " + colourNumber + " for the Patchwork " \
    + "(must be 'red' or 'green', or 'blue' or 'magenta' or 'cyan') "
    colour = str(input(promt))
    colour = checkRecognisedColour(colour)
    return colour

#Checks the colour is valid
def checkRecognisedColour(colour):
    coloursList = ["red", "green", "blue", "magenta", "cyan"]
    while not colour in coloursList:
        promt = "Please enter a valid colour for the Patchwork " \
        + "(must be 'red' or 'green', or 'blue' or 'magenta' or 'cyan') "
        colour = str(input(promt))
    return (colour)

#Checks two colours are not the same
def checkNotSameColours(colourA, colourB):
    promt = "Please enter a different colour. The colour " + colourA + " has already been used " + "(must be 'red' or 'green', or 'blue' or 'magenta' or 'cyan')"
    change = False
    if colourA == colourB:
        while colourA == colourB:
            colourB = str(input(promt))
            colourB = checkRecognisedColour(colourB)
            change = True
    return (colourB, change)

#Draws multiple patches based on the user input
def drawPatchwork(window, numberAcross, numberUp, colourOne, colourTwo, colourThree):
    patchNumber = 0
    patchColumn = 0
    for y in range(0, numberUp * height, height):
        patchColumn = patchColumn + 1
        patchRow = 0
        for x in range(0, numberAcross * width, width):
            patchRow = patchRow + 1
            patchNumber = patchNumber + 1
            currentColour = generateCurrentColour(patchNumber, colourOne, colourTwo, colourThree)
            patch = getPatchType(patchRow, patchColumn)
            if patch == "patch2" :
                drawFinalPatch5(window, x + margin, y + margin, currentColour, "append")
            elif patch == "patch1":
                drawPenultimatePatch4(window, x + margin, y + margin, currentColour, "append")

#returns the colour that the current patch should be drawn in
def generateCurrentColour(patchNumber, colour1, colour2, colour3):
    if patchNumber % 3 == 1:
        return colour1
    elif patchNumber % 3 == 2:
        return colour2
    elif patchNumber % 3 == 0:
        return colour3

#returns the current patch that should be drawn
def getPatchType(patchRow, patchColumn):
    if (patchRow + patchColumn) % 2 == 0 :
                return "patch2"
    else:
                return "patch1"

#Draws the first patch in the given positon and colour
def drawFinalPatch5(window, xCoordinate, yCoordinate, colour, list):
    borderX = xCoordinate
    borderY = yCoordinate
    radius = 10
    diameter = 2 * radius
    for y in range(0, 100, diameter):
        for x in range(0, 100, diameter):
            centre = Point( borderX + x + radius, borderY + y + radius )
            circle = Circle(centre, radius)
            circle.setOutline(colour)
            if y == 1 * diameter or y == 3 * diameter:
                circle.setFill("white")
            else:
                circle.setFill(colour)
            circle.draw(window)
    if list == "append":
        patchTypeList.append("patch1")
        coloursList.append(colour)

#Draws the second patch in the given positon and colour
def drawPenultimatePatch4(window, xCoordinate, yCoordinate, colour, list):
    borderX = xCoordinate
    borderY = yCoordinate
    radius = 10
    diameter = 2 * radius
    for y in range(0, 100, diameter):
        for x in range(0, 100, diameter):
    #Draw filled in circles
            centre = Point( borderX + x + radius, borderY + y + radius )
            circle = Circle(centre, radius)
            circle.setOutline(colour)
            circle.setFill(colour)
            circle.draw(window)
    #Draw  white Rectangles to cover up half of circles
            if x % 40 == 0:
                Point1 = Point(borderX + x, borderY + y)
                Point2 = Point(borderX + x + radius, borderY + y + diameter)
            else:
                Point1 = Point(borderX + x, borderY + y + radius)
                Point2 = Point(borderX + x + diameter, borderY + y + diameter)
            rectangle = Rectangle(Point1, Point2)
            rectangle.setFill("white")
            rectangle.setOutline("white")
            rectangle.draw(window)
    #Draw circle outlines
            centre = Point( borderX + x + radius, borderY + y + radius )
            circle = Circle(centre, radius)
            circle.setOutline(colour)
            circle.draw(window)
    if list == "append":
        patchTypeList.append("patch2")
        coloursList.append(colour)


#The following code allows the advanced program feature to work:

#This function allows the User to click on two patches to swap them over
def allowSwappingPatches(window, numberAcross, colourOne, colourTwo, colourThree):
    while True:
#Highlight first patch when clicked
        positionFirst = window.getMouse()
        positionFirstX, positionFirstY = getPatchPosition(positionFirst)
        patchNumberFirst, patchTypeFirst, colourFirst = getPatchDetails(positionFirstX, positionFirstY, numberAcross)
        highlightPatch(window, positionFirstX, positionFirstY, patchTypeFirst, colourFirst)
#Swap pacthes when second patch is clicked
        positionSecond = window.getMouse()
        positionSecondX, positionSecondY = getPatchPosition(positionSecond)
        patchNumberSecond, patchTypeSecond, colourSecond = getPatchDetails(positionSecondX, positionSecondY, numberAcross)
        switchPatches(window, patchNumberFirst, positionFirstX, positionFirstY, patchTypeFirst, colourFirst, patchNumberSecond, positionSecondX, positionSecondY, patchTypeSecond, colourSecond)

#Finds the position of the patch that has been clicked on
def getPatchPosition(position):
    positionX = math.floor((position.getX() - margin ) /100) * 100
    positionY = math.floor((position.getY() - margin) /100) * 100
    return positionX, positionY

#Return the details of the patch that has been click on
def getPatchDetails(positionX, positionY, numberUp):
    patchNumber = (positionY/100) * numberUp + positionX/100 + 1
    patchType = patchTypeList[int(patchNumber) - 1]
    currentColour = coloursList[int(patchNumber) - 1]
    return patchNumber, patchType, currentColour

#Darkens the colour of the first patch click on
def highlightPatch(window, xCoord, yCoord, patchType, colour):
    newColour = colour + "4"
    if patchType == "patch1":
        drawFinalPatch5(window, xCoord + margin, yCoord + margin, newColour, "leave")
    elif patchType == "patch2":
        drawPenultimatePatch4(window, xCoord + margin, yCoord + margin, newColour, "leave")

#Draws the first patch with the colour and design of the second and visa versa
def switchPatches(window, firstPatchNumber, positionFirstX, positionFirstY, patchTypeFirst, colourFirst, secondPatchNumber, positionSecondX, positionSecondY, patchTypeSecond, colourSecond):
    drawPatch(window, positionFirstX, positionFirstY, patchTypeSecond, colourSecond)
    drawPatch(window, positionSecondX, positionSecondY, patchTypeFirst, colourFirst)
#Updates the various lists with the new data
    coloursList[int(firstPatchNumber - 1)] = colourSecond
    coloursList[int(secondPatchNumber - 1)] = colourFirst
    patchTypeList[int(firstPatchNumber - 1)] = patchTypeSecond
    patchTypeList[int(secondPatchNumber - 1)] = patchTypeFirst

#Redraws a Patch given, the patch design, colour and positon.
def drawPatch(window, positionX, positionY, patchType, colour):
    if patchType == "patch1":
        drawFinalPatch5(window, positionX + margin, positionY + margin, colour, "leave")
    elif patchType == "patch2":
        drawPenultimatePatch4(window, positionX + margin, positionY + margin, colour, "leave")

main()

