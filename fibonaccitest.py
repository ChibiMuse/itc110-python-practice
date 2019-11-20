#fibbonaccitest.py
#A program to calculate the nth fibonnaci term
# by Megan Smith

def main():
    try:
        x = 1
        z = 1
        y = 1
        i = eval(input("Please enter the sequence number:"))
        #if and elif statements makes sure that the input is a valid sequence number.
        if i <= 0:
            print("Please enter a whole number greater than 0.")
            main()
        elif (i % 1) != 0:
            print("Please enter a whole number.")
            main()
        elif i < 941:
            s = i
            i = i + 1
            sequence = fibRecursive(i,x,z,y)
            suffixFormat(s, sequence)
            runAgain()
        elif i > 940:
            print("Please choose a smaller number.")
            main()
    except:
        print("Please enter a whole number without other characters.")
        main()

#Recursive function takes in the nth term and outputs the appropriate fibonacci number
def fibRecursive(i,x,z,y):
    i = i - 1
    if i <= 2:
        return(z)
    else:
        z = x + y
        y = x
        x = z
        return fibRecursive(i,x,z,y)

#Function to make sure the the "nth" term is proper grammatical form.
#It searches for single digits first, and then will filter out anything with "1"
# in the 10s places since those don't follow the "1st", "2nd", "3rd" pattern.
def suffixFormat(s, sequence):
    suffix = str(s)
    if len(suffix) <= 1:
        if suffix[-1] == "1":
            print("The {0}st Fibonacci number is {1}".format(suffix, sequence))
        elif suffix[-1] == "2":
            print("The {0}nd Fibonacci number is {1}".format(suffix, sequence))
        elif suffix[-1] == "3":
            print("The {0}rd Fibonacci number is {1}".format(suffix, sequence))
        else:
            print("the {0}th Fibonacci number is {1}".format(suffix, sequence))
    else:
        if suffix[-2] == "1":
            print("The {0}th Fibonacci number is {1}".format(suffix, sequence))
        elif suffix[-1] == "1":
            print("The {0}st Fibonacci number is {1}".format(suffix, sequence))
        elif suffix[-1] == "2":
            print("The {0}nd Fibonacci number is {1}".format(suffix, sequence))
        elif suffix[-1] == "3":
            print("The {0}rd Fibonacci number is {1}".format(suffix, sequence))
        else:
            print("the {0}th Fibonacci number is {1}".format(suffix, sequence))
            
#A function to ask the user if they would like to continue using the program
def runAgain():
    answer = input("Run again? y/n : ")
    if answer == "y" or answer == "Y":
        main()
    else:
        print("Ending Program. Goodbye.")
        
main()
        
