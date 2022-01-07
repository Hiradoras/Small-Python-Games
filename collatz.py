

def collatz(number):
    try:
        number = int(number)
        while number != 1:
            if number % 2 == 0:
                print(number//2)
                collatz(number//2)
            else:
                print((number * 3) + 1)
                collatz((number * 3) + 1)
            break        
        
    except ValueError:
        new_number = input("Please enter an integer: ")
        collatz(new_number)




x = input("Enter a number: ")
collatz(x)

        