# pikachumaker.py
#A program that creates three pikachus of different sizes.
# by Megan Smith

from graphics import *
import random

win = GraphWin("Pikachu Faces", 400, 400)
win.setBackground("white")

def main():
    start = win.getMouse()
    x = start.getX()
    y = start.getY()
    drawPikachu(x,y)



def drawPikachu(x,y):
    #draws pikachu
    ovalx = 1.74
    ovaly = 3.6

    #Pikachu head
    head = Oval(Point(x * ovalx, y * ovaly),Point(x,y))
    head.setFill("yellow")
    headCenter = head.getCenter()
    print(headCenter)
    head.draw(win)

