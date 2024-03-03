import random

while(True):
    print(random.randint(1,6))
    another_roll = input("Do you want to roll the dice again (y/n)?\n")
    if another_roll =='y':
        continue
    else:
        break


