def main():
    mpg()

def mpg():
    print("This program will calculate your MPG.")
    milesDriven = float(input("Please enter the miles traveled:"))
    gallonsUsed = float(input("Please enter the gallons of gas used:"))

    mpg = round((milesDriven/gallonsUsed),2)

    print("Your Miles Per Gallon:\t" + str(mpg))

main()
    
