def main():
    try:
        x = 1
        z = 1
        y = 1
        i = eval(input("Please enter the sequence number:"))
        if i <= 0:
            print("Please enter a whole number greater than 0.")
            main()
        elif (i % 1) != 0:
            print("Please enter a whole number.")
            main()
        elif i < 10000:
            i = i + 1
            fib_recursive(i,x,z,y)
        elif i > 9999:
            print("Please choose a smaller number.")
            main()
    except:
        print("Please enter a whole number without other characters.")
        main()

def fib_recursive(i,x,z,y):
    i = i - 1
    if i <= 2:
        print(z)
    else:
        z = x + y
        y = x
        x = z
        return fib_recursive(i,x,z,y)
        
main()
        
