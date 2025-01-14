import random

lowest_number = 1;
highest_number = 10;

answer = random.randint(lowest_number, highest_number)
guesses = 0

while True:
    user_answer = int(input(f"Enter any number between {lowest_number} and {highest_number} (Enter 0 to exit): "))
    if user_answer == 0:
        print("Exiting the game. Thanks for playing!")
        break
    elif user_answer == answer:
        print("Congratulations! You won!")
        print(f"Number of guesses: {guesses}")
        break
    elif user_answer < answer:
        print("Too low. Try again.")
        guesses += 1
    elif user_answer > answer:
        print("Too high. Try again.")
        guesses += 1
    else:
        print("Invalid input. Please enter a number.")