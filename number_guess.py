#Here is the number that wanted to be guess correctly by user 

from random import randint

determined_number=randint(1,100)

while True :
    user_guess=int(input("Take a guess between 1-100:"))
    if user_guess == determined_number :
        print("you did guess correctly the number.")
        break
    elif user_guess > determined_number :
        print("determined number is lesser than what you did choose.")
    elif  user_guess < determined_number :
        print("determined number is greater than what you did choose .")
