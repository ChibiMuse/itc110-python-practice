#kilotomilesconvert.py
#   A program to convert kilometers to miles.
# by: Megan Smith

#The conversation formula for kilometers to miles 1 kilometer = .621371 miles
def main():
    print("The distance is " + str(float(kiloVar)*.621371) + " miles.")

print("This program converts kilometers to miles.")

#Request for user kilometer input
#Throws up an error message if they enter anything that isn't a number.
while True:
    try:
        kiloVar = float(input("Please enter distance in kilometers:"))
        break
    except ValueError:
        print("Distances can only be in numbers. Please try again!")

main()

