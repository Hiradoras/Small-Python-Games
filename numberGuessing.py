import random, sys
print("Welcome to the number guessing game!")
x = (random.randint(0,20))
while True:
    guess = int(input("Guess the number between 0-20: "))
    if guess > x:
        print("Your guess is bigger than the number. Try again!")
        continue
    elif guess < x:
        print("Your guess is smaller than the number! Try again!")
        continue
    else:
        print("Congrats! You won! Wanna play again?")
        again = input("'Y' for yes and 'N' for no: ")
        if again.upper() == "Y":
            x = (random.randint(0,20))
            continue
        elif again.upper() == "N":
            print("good bye!!!")
            sys.exit()
