#Programs that calculate the averages of numbers.


#call the program from main.
def main():
    average_list()

#The first program is for a set amount of three numbers.
def average():
    x,y,z = eval(input("Enter the three numbers you wish to average, seperated by commas (no spaces)"))
    average = (x + y + z)/3
    print("The average of ", x, ", ", y, ", and ", z, "is:", round(average,2),".")

#The second program is more flexible for a user defined amount of numbers.
def average_list():
    print("This program calculates the average of a set amount of numbers.")
    total = 0
    averageList = []
    n = int(input("Enter the number of  numbers you wish to average:"))
    #gets the numbers from the user input and puts them into a list.
    for i in range(0,n):
        itemsEach = int(input("Enter the numbers you wish to average:"))
        
        averageList.append(itemsEach)
    #totals the list
    for i in averageList:
        total += i
    #finds the average
    average = total/n
    print("Total:", round(total,2))    
    print("Average:", round(average,2))
    
main()
