#winterscene.py
#A program to draw a winter scene
# By Megan Smith

from graphics import *
import random

#sets up window size and background color
win = GraphWin("Winter Scene",400,400)
win.setCoords(0,0,400,400)
win.setBackground("powder blue")

#draws snow on the ground
snowCenter = Point(10,0)
snow = Circle(snowCenter, 15)
snow.setFill("snow")
snow.setOutline("snow")
snow.draw(win)
snowclone={}
for i in range(30):
   snowclone[i]= snow.clone()
   snowclone[i].move(random.randint(0,400),0)
   snowclone[i].draw(win)
snowball = Circle(snowCenter, 20)
snowball.setFill("snow")
snowball.setOutline("snow")
snowball.draw(win)
snowballclone={}
for i in range(30):
    snowballclone[i] = snowball.clone()
    snowballclone[i].move(random.randint(0,400),0)
    snowballclone[i].draw(win)

#draws snowflakes
snowflake = Circle(Point(5, 5), 2)
snowflake.setFill("snow")
snowflake.setOutline("snow")
snowflake.draw(win)
snowflakeclone={}
for i in range (500):
    snowflakeclone[i] = snowflake.clone()
    snowflakeclone[i].move(random.randint(0,400),random.randint(0,400))
    snowflakeclone[i].draw(win)

#draws pikachu
x1 = 100
x2 = 130
x3 = 145
x4 = 135

y1 = 200
y2 = 155
y3 = 75
y4 = 145

#Pikachu body
body = Polygon(Point(184,39), Point(139,39), Point(135,0), Point(188,0))
body.setFill("yellow")
body.draw(win)

#Pikachu ears 
leftEar = Polygon(Point(100,160), Point(100,115), Point(130,75), Point(145,75), Point(135,105))
leftEar.setFill("yellow")
leftEar.draw(win)
leftEartip = Polygon(Point(100,160), Point(100,115), Point(135,105))
leftEartip.setFill("black")
leftEartip.draw(win)

rightEar = Polygon(Point(200,160), Point(210,115), Point(185,75), Point(175,75), Point(180,105))
rightEar.setFill("yellow")
rightEar.draw(win)
rightEartip = Polygon(Point(200,160), Point(210, 115), Point(180,105))
rightEartip.setFill("black")
rightEartip.draw(win)

#Pikachu head
head = Oval(Point(200,90),Point(115,25))
head.setFill("yellow")
headCenter = head.getCenter()
print(headCenter)
head.draw(win)

eyeCenter = Point(145.25,55.5)
leftEye = Circle(eyeCenter, 6)
leftEye.setFill("black")
leftEye.draw(win)

rightEye = leftEye.clone()
rightEye.move(31.25,0)
rightEye.draw(win)

pupilCenter = Point(143,57.5)
leftPupil = Circle(pupilCenter,4)
leftPupil.setFill("white")
leftPupil.draw(win)

rightPupil = leftPupil.clone()
rightPupil.move(31.25,0)
rightPupil.draw(win)

noseBottom = Point(162.5, 43)
nose = Polygon(Point(159, 45), Point(165, 45), noseBottom)
nose.setFill("magenta")
nose.draw(win)

# For Pikachu's mouth, mouth1 is the center line, mouth2/3 are the branches down from the center line.
# The smile is the two upturned lines of his mouth.
mouthBottom = Point(162.5, 41)
mouthLeft = mouthBottom.clone()
mouthLeft.move(-4,-3)
mouthRight = mouthBottom.clone()
mouthRight.move(4,-3)
mouth1 = Line(noseBottom, mouthBottom)
mouth2 = Line(mouthBottom, mouthLeft)
mouth3 = Line(mouthBottom, mouthRight)
mouth1.draw(win)
mouth2.draw(win)
mouth3.draw(win)
smileLeft = mouthLeft.clone()
smileLeft.move(-3,2)
smileRight = mouthRight.clone()
smileRight.move(3,2)
smile1 = Line(mouthLeft, smileLeft)
smile2 = Line(mouthRight, smileRight)
smile1.draw(win)
smile2.draw(win)

leftCheek = Circle(Point(139,39), 7)
leftCheek.setFill("red")
leftCheek.draw(win)

rightCheek = leftCheek.clone()
rightCheek.move(45,0)
rightCheek.draw(win)

#Draws Pikachu's winter hat
hat = Polygon(Point(135,80),Point(185,80), Point(160,165))
hat.setFill("red")
hat.draw(win)

hatFur = Circle(Point(135,80),8)
hatFur.setFill("white")
hatFur.setOutline("white")
hatFur.draw(win)

hatFurtop = Circle(Point(160,165), 10)
hatFurtop.setFill("white")
hatFurtop.setOutline("white")
hatFurtop.draw(win)

hatFurclone={}
x = 10
for i in range(5):
    hatFurclone[i] = hatFur.clone()
    hatFurclone[i].move(x,0)
    hatFurclone[i].draw(win)
    x = x + 10

#draws the message
message = Text(Point(200,300),"Winter Scene Fun!")
message.setFace("times roman")
message.setStyle("bold italic")
message.setSize(22)
message.draw(win)

