import random

options = ("rock", "paper", "scissors")
playing = True

while playing:
    player = input("Enter a choice (rock, paper, scissors) or 'quit' to stop: ").lower()
    if player == "quit":
        playing = False
        print("Thanks for playing!")
        break
    if player not in options:
        print("Invalid choice. Please try again.")
        continue

    computer = random.choice(options)

    if player == computer:
        print(f"Computer chose {computer}. Player chose {player}. It's a Tie!")
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        print(f"Computer chose {computer}. Player chose {player}. You Win!")
    else:
        print(f"Computer chose {computer}. Player chose {player}. You Lose!")
