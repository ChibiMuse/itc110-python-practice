# weeklypay.py
# A program to calculate your weekly pay based on hourly pay rate.
# by Megan Smith

#calls getPay() and getHours() and passes those variables to calculatePay(pay, hours)
def main():
    print("This program calculates your weekly pay.\n")
    x = getPay()
    y = getHours()
    total = calculatePay(x, y, z)
    print("Your weekly pay is: ${0:.2f}".format(total))

#function to get wage info from user
def getPay():
    try:
        pay = float(input("Enter hourly wage: $"))
        return pay
    except:
        print("Please try again.")
        x = getPay()
        return x

#function to get hours from user
def getHours():
    try:
        hours = float(input("Enter hours worked: "))
        return hours
    except:
        print("Please try again.")
        y = getHours()
        return y

#function that takes two parameters (pay and hours) and returns the hourly pay.
def calculatePay(pay, hours):
    total = pay * hours
    return total

main()
