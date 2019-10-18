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

#draws pikachu head
x1 = 100
x2 = 130
x3 = 145
x4 = 135

y1 = 200
y2 = 155
y3 = 75
y4 = 145
 
leftEar = Polygon(Point(100,200), Point(100,155), Point(130,75), Point(145,75), Point(135,145))
leftEar.setFill("yellow")
leftEar.draw(win)
leftEartip = Polygon(Point(100,200), Point(100,155), Point(135,145))
leftEartip.setFill("black")
leftEartip.draw(win)
rightEar = 




    


    
