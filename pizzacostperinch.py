#pizza_cost.py
#by Megan Smith
#A simple program that calculates the cost per square inch of pizza.
#imported library:
from math import pi

#main function the describes the program being called
def main():
    print("This program calculates the cost per square inch of pizza!")
    pizza_cost()

def pizza_cost():
    try:
        #input
        pizzaSize = int(input("Enter the diameter of the pizza (in inches):"))
        pizzaCost = float(input("Enter the cost of the pizza (in dollars):"))
        #process the radius
        radius = pizzaSize/2
        #process the area
        area = pi * (radius*radius)
        #process the cast per sq inch
        costPer = round(pizzaCost/area, 2)
        #output
        print("The", str(pizzaSize),"inch pizza cost ${:.2f}".format(round(pizzaCost,2))+".")
        print("Cost per square inch: ${:.2f}".format(round(costPer,2))+"/inch")
        input("Press <Enter> to end")
     #catches any errors and has the user try again.   
    except:
        print("Please enter a whole number without other characters.")
        pizza_cost()


main()
        
        
