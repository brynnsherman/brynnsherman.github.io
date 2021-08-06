"""
Sami Yousif
CodeNamesGenerator
11/18/18, 5:22 PM

Updated 12/20/18 by Brynn Sherman
- added in iterations/saving
"""
from __future__ import division
import random
from psychopy import visual, core, data, event, gui
import psychopy
import math
from random import shuffle
import time
import os  # handy system and path functions
# import win32api

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Setup the Window
win = visual.Window(size=(650, 650), units = 'pix', fullscr=False, screen=0, allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[181,172,148], colorSpace='rgb255', blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it successfully

squareSize = 90
cornerSize = 100

signalSquare = visual.Rect(win, units='pix', width=590, height=590, lineWidth=4, lineColorSpace='rgb255', lineColor=[0,0,255], fillColorSpace='rgb255',fillColor=[127,121,104], pos=(0,0), opacity=1)
blackBackground = visual.Rect(win, units='pix', width=550, height=550, lineWidth=0, lineColorSpace='rgb255', lineColor=[0,0,0], fillColorSpace='rgb255',fillColor=[0,0,0], pos=(0,0), opacity=1)


xPos = [-200,-100,0,100,200]
yPos = [-200,-100,0,100,200]
numSquares = len(xPos)*len(yPos)
squareDic = {}
for i in range(len(xPos)):
    for j in range(len(yPos)):
        squareName = "square" + str((i*5)+(j+1))
        shape = visual.Rect(win, units='pix', width=squareSize, height=squareSize, lineWidth=3, lineColorSpace='rgb255',lineColor=[0,100,255], fillColorSpace='rgb255',fillColor=[0,0,0], pos=(xPos[i],yPos[j]), opacity=1)
        squareDic[squareName] = shape

# print squareDic
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

def createBoard(numRed,numBlue,numBlack,numPurple,numGreen,numOrange,boardKind,n): #routine for the core of the experiment, used for practice trials and actual exp
    totalNumber = numSquares
    numWhite = totalNumber - (numRed+numBlue+numBlack+numPurple+numGreen+numOrange)
    redProb,blueProb,blackProb,purpleProb,greenProb,orangeProb,whiteProb = numRed/totalNumber, numBlue/totalNumber,numBlack/totalNumber,numPurple/totalNumber, numGreen/totalNumber, numOrange/totalNumber, numWhite/totalNumber
    # print redProb,blueProb,blackProb,purpleProb,greenProb,orangeProb,whiteProb
    redCounter, blueCounter, blackCounter, purpleCounter, greenCounter, orangeCounter, whiteCounter = 0,0,0,0,0,0,0

    listCount = [[None,numWhite,[181,172,148],[127,121,104]],["diamond2.png",numRed,[210,50,50],[210,100,100]],["circle2.png",numBlue,[0,0,255],[0,100,255]],["x.png",numBlack,[75,75,75],[100,100,100]],["square2.png",numPurple,[111,6,200],[142,8,255]],["q.png",numGreen,[0,175,0],[0,215,0]],["triangles.png",numOrange,[255,160,0],[255,192,0]]]
    theList = []
    for color in listCount:
        for i in range(color[1]):
            theList.append([color[2],color[3],color[0]])
    shuffle(theList)

    if numRed > numBlue:
        signalColor = [210,50,50]
    else:
        signalColor = [0,0,255]
    signalSquare.setLineColor(signalColor)
    signalSquare.draw()
    blackBackground.draw()
    for i in range(numSquares):
        # print i
        squareName = "square" + str(i+1)
        squareDic[squareName].setFillColor(theList[i][0])
        squareDic[squareName].setLineColor(theList[i][1])
        findX = int(math.floor(i/5))
        findY = int(i % 5)
        squareDic[squareName].draw()
        newImage = visual.ImageStim(win, image=theList[i][2], units='pix', pos=(xPos[findX],yPos[findY]), size=60, opacity=1.0)
        newImage.draw()

    win.getMovieFrame(buffer='back')
    win.flip()
    time.sleep(.25)

    fileName = (boardKind + "_" + str(n) + ".png")

    win.saveMovieFrames(fileName)

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

for i in range(50):
    createBoard(9,8,3,0,0,0,"Black",i) #RED, BLUE, BLACK, PURPLE, GREEN, ORANGE

for i in range(50,100):
    createBoard(8,9,3,0,0,0,"Black",i)

for i in range(50):
    createBoard(9,8,1,2,0,0,"Purple",i) #RED, BLUE, BLACK, PURPLE, GREEN, ORANGE

for i in range(50,100):
    createBoard(8,9,1,2,0,0,"Purple",i)

for i in range(50):
    createBoard(9,8,1,0,2,0,"Green",i) #RED, BLUE, BLACK, PURPLE, GREEN, ORANGE

for i in range(50,100):
    createBoard(8,9,1,0,2,0,"Green",i)

for i in range(50):
    createBoard(9,8,1,0,0,2,"Orange",i) #RED, BLUE, BLACK, PURPLE, GREEN, ORANGE

for i in range(50,100):
    createBoard(8,9,1,0,0,2,"Orange",i)

for i in range(50):
    createBoard(9,8,2,2,2,2,"Crazy",i) #RED, BLUE, BLACK, PURPLE, GREEN, ORANGE

for i in range(50,100):
    createBoard(8,9,2,2,2,2,"Crazy",i)
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

win.close()
core.quit()
