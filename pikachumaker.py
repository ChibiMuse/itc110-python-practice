# pikachumaker.py
# A program that creates pikachu faces of different sizes where you click your mouse.
# by Megan Smith

from graphics import *
import random

#Sets up the graphic window
win = GraphWin("Pikachu Faces", 500, 500)
win.setCoords(0,0,500,500)
win.setBackground("white")


def main():
    numList = [.25, .5, .75, 1, 2, 3, 4] #Controls the variables for Pikachu Size to avoid divide by 0 error.
    #Calls for mouse clicks and runs the drawPikachu function each time.
    for i in range(10):
        start = win.getMouse()
        x = start.getX()
        y = start.getY()
        sizeNum = numList[random.randint(0,6)]
        drawPikachu(x,y, sizeNum) # call to draw pikachu which pass the x & y of the mouse as well as the random size multiplier
    win.getMouse()


#The draw pikachu function that needs to be passed 3 parameters. An X value. A Y value, and
#a number (div) which is used to divide the x and y values by to control the size (2 would be half sized and .5 would be 2 times as big)    
def drawPikachu(x,y,div):
    #Starting values to get the proportions correct
    #All points are written as they relate to +/- of x or y.
    x = x + (42.5 /div)
    y = y + (32.5 /div)
    ovalx = 85/div
    ovaly = 65/div

    #Pikachu Ears
    a = x - (100/div)
    b = y + (70 /div)
    c = y + (25 /div)
    d = x - (70 /div)
    e = y - (15 /div)
    f = x - (55 /div)
    g = x - (65 /div)
    h = y + (15 /div)

    earLa = Point(a, b)
    earLb = Point(a, c)
    earLc = Point(d, e)
    earLd = Point(f, e)
    earLe = Point(g, h)

    leftEar = Polygon(earLa, earLb, earLc, earLd, earLe)
    leftEar.setFill("yellow")
    leftEar.draw(win)
    leftEartip = Polygon(earLa, earLb, earLe)
    leftEartip.setFill("black")
    leftEartip.draw(win)

    aa = x + (10 /div)
    bb = x - (15 /div)
    cc = x - (25 /div)
    dd = x - (20 /div)

    earRa = Point(x, b)
    earRb = Point(aa,c)
    earRc = Point(bb, e)
    earRd = Point(cc, e)
    earRe = Point(dd, h)

    rightEar = Polygon(earRa, earRb, earRc, earRd, earRe)
    rightEar.setFill("yellow")
    rightEar.draw(win)
    rightEartip = Polygon(earRa, earRb, earRe)
    rightEartip.setFill("black")
    rightEartip.draw(win)

    #Pikachu Head & Face
    head = Oval(Point(x, y), Point(x-ovalx,y-ovaly))
    head.setFill("yellow")
    headCenter = head.getCenter()
    head.draw(win)

    eyeCenter = Point(x-(54.75 /div), y - (34.5 /div))
    leftEye = Circle(eyeCenter, (6/div))
    leftEye.setFill("black")
    leftEye.draw(win)

    rightEye = leftEye.clone()
    rightEye.move((31.25/div),0)
    rightEye.draw(win)

    pupilCenter = Point(x - (57 /div), y - (32.5 /div))
    leftPupil = Circle(pupilCenter,(4/div))
    leftPupil.setFill("white")
    leftPupil.draw(win)

    rightPupil = leftPupil.clone()
    rightPupil.move((31.25/div),0)
    rightPupil.draw(win)

    noseBottom = Point(x - (37.5 /div), y - (47 /div))
    nose = Polygon(Point(x - (41 /div), y - (45/ div)), Point(x - (35 /div), y - (45 / div)), noseBottom)
    nose.setFill("magenta")
    nose.draw(win)

    # For Pikachu's mouth, mouth1 is the center line, mouth2/3 are the branches down from the center line.
    # The smile is the two upturned lines of his mouth.
    mouthBottom = Point(x - (37.5 /div), y - (49 /div))
    mouthLeft = mouthBottom.clone()
    mouthLeft.move(-4/div,-3/div)
    mouthRight = mouthBottom.clone()
    mouthRight.move(4/div,-3/div)
    mouth1 = Line(noseBottom, mouthBottom)
    mouth2 = Line(mouthBottom, mouthLeft)
    mouth3 = Line(mouthBottom, mouthRight)
    mouth1.draw(win)
    mouth2.draw(win)
    mouth3.draw(win)
    smileLeft = mouthLeft.clone()
    smileLeft.move(-3/div,2/div)
    smileRight = mouthRight.clone()
    smileRight.move(3/div,2/div)
    smile1 = Line(mouthLeft, smileLeft)
    smile2 = Line(mouthRight, smileRight)
    smile1.draw(win)
    smile2.draw(win)

    leftCheek = Circle(Point(x - (61 /div), y - (51 /div)), 7/div)
    leftCheek.setFill("red")
    leftCheek.draw(win)

    rightCheek = leftCheek.clone()
    rightCheek.move(45/div,0)
    rightCheek.draw(win)

main()

