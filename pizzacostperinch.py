#pizza_cost.py
#by Megan Smith
#A simple program that calculates the cost per square inch of pizza.
#imported library:
from math import pi

#main function the describes the program being called
def main():
    print("This program calculates the cost per square inch of pizza!")
    pizza_cost()
    
#a function to return the area of a circle when given the radius
def areaFunc(radius):
	area = pi * radius**2
	return area

#a function to return the radius of a given diameter
def radiusFunc(diameter):
    radius = diameter/2
    return radius

def pizza_cost():
    try:
        #input
        pizzaSize = float(input("Enter the diameter of the pizza (in inches):"))
        pizzaCost = float(input("Enter the cost of the pizza (in dollars):"))
        #process the radius
        radius = radiusFunc(pizzaSize)

        #process the area
        area = areaFunc(radius)
        #process the cost per sq inch

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
        
