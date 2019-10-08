#kilotomilesconvert.py
#   A program to convert kilometers to miles.
# by: Megan Smith

#The conversation formula for kilometers to miles 1 kilometer = .621371 miles

def main():
    print("This program converts kilometers to miles")
    km_miles()

def km_miles():
    #input
    try:
        kiloVar = eval(input("Please enter distance in kilometers:"))
        #processing
        miles = kiloVar * .621371
        #output
        print("The distance is", miles, "miles.")
    except:
        print("Distances can only be in numbers. Please try again.")
        km_miles()

main()

