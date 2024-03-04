import random

options = ("rock" , "paper", "scissor")
player = None
player = input("Enter the choice:\n")
if player not in options:
    print("Choose from the 3 choices only!!")
else:
    computer = random.choice(options)
    print(f"Player : {player}")
    print(f"Computer: {computer}")

    if player==computer:
        print("Its a Tie!")
    elif player=="rock" and computer =="scissor":
        print("You Win!")
    elif player=="paper" and computer =="rock":
        print("You Win!")
    elif player=="scissor" and computer =="paper":
        print("You Win!")
    else:
        print("You Lose!")