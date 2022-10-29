"""
DICE ROLLING SIMULATOR

One that reaches first 36 points by rolling the dice  will win the game.

"""
#To import randint function from the library will enable the computer "roll" the dice .

from random import randint

total_co=0 # it is the variable that stands for computer's score

total_us=0 # it is the variable that stands for user's score

while max(total_co,total_us) < 36 :
    user_dice=input("Type in 'R' for rolling the dice :")
    if user_dice == "R" :
        user_integer=randint(1,6)
        print("What number does dice show for user:",user_integer)
        total_us += user_integer

        computer_integer=randint(1,6)
        print("What numbers does dice show for computer:",computer_integer)
        total_co += computer_integer
    
    else:
        print("You must type in 'R' to roll the dice .")



if max(total_co,total_us) == total_us :
    print("The user won with",total_us,"points.")

else:
    print("The computer won with",total_co,"points.")


