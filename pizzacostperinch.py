#pizza_cost.py
#by Megan Smith
#A simple program that calculates the cost per square inch of pizza.


def main():
    print("This program calculates the cost per square inch of pizza!")
    pizza_cost()

def pizza_cost():
    pie = 3.14159
    try:
        pizzaSize = int(input("Enter the diameter of the pizza (in inches):"))
        pizzaCost = float(input("Enter the cost of the pizza (in dollars):"))
        radius = pizzaSize/2
        area = pie * (radius*radius)
        costPer = round(pizzaCost/area, 2)
        print("The", str(pizzaSize),"inch pizza cost ${:.2f}".format(round(pizzaCost,2))+".")
        print("Cost per square inch: ${:.2f}".format(round(costPer,2))+"/inch")
        input("Press <Enter> to end")
        
    except:
        print("Please enter a whole number without other characters.")
        pizza_cost()


main()
        
        
