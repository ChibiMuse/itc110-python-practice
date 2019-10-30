#wordcount.py
#A program to count the number of words in a user generated sentence.
# by Megan Smith

from graphics import *

def main():
    win = GraphWin("Word Counter", 500, 400)
    win.setCoords(0.0, 0.0, 3.0, 4.0)

    Explain = Text(Point(1,3), "This program counts the number of words (separated by spaces) in the text you enter.").draw(win)
    Text(Point(1,1), "Please enter your text: ").draw(win)
    input = Entry(Point (2,1), 5)
    input.draw(win)
    Explain.undraw()
    output = Text(Point(1,3), " ")
    output.draw(win)

    #wait for mouse click
    win.getMouse()

    #print("This program counts the number of words (separated by spaces) in the text you enter.\n")
    text = input.getText()
    x = countWords(text)
    output.setText(x)
    button.setText("Quit")

def countWords(text):
    textList = text.split(" ")
    x = 0
    for i in textList:
        x += 1
    return x
    #print("The total word count is: {0} ".format(str(x)))

main()
    
    
    
