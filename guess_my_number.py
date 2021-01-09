# Generation of Random Number
from random import randint

# Text prompting the user for input
print('Hello There, Welcome to Guess the number!')
print(
    "Please input your chosen range of integers. Once you have input your guesses, we will let you know if you're correct.\n")
# Actual request for input that opens prompt
min = None
start_range = None
while type(min) is not int:
    min = input("Enter a minimum number for the range: ")
    if min.isdigit():
        min = int(min)
    else:
        print("Please enter a valid integer")
print("")

max = min - 1
while type(max) is not int or max < min:
    max = input("Enter a maximum number for the range: ")
    if max.isdigit():
        max = int(max)
        if max < min:
            print("The max number has to be greater than the min!")
    else:
        print("Please enter a valid integer")
    #checks if the inputted max is greater than the inputted min


print("\nThank you your range has been accepted!")

random_num = randint(min, max)

# ask user to input their guess
guess = ""
#check if guess is a digit
check = guess.isdigit()
#set number of guesses at 0
num_of_guesses = 0
while check == False or guess != random_num:
    guess = input("Enter your guess: ")
    num_of_guesses += 1
    check = guess.isdigit()
    if guess.isdigit():
        guess = int(guess)
        if guess == random_num:
            #will print congratulations, stop loop and print # of guesses
            print("Congratulations! You guessed the number in {} tries!\n".format(num_of_guesses))
            break
        elif guess < random_num:
            print("Incorrect. The number you guessed is lower!\n")
        elif guess > random_num:
            print("Incorrect. The number you guessed is higher!\n")
    else:
        print("Error that is not a valid integer!")
