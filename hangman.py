"""

Description of the Game;
User will play the game with the computer.Firstly one word randomly will be determined afterwards user will try to guess the word within the limited contidion

"""

# User has 6 wrong guess right.

# User will play with the computer


import random

words = ["competition","selfless","phenomenon","right"] # Computer will randomly choose a word from this given list.


word_selector = random.randint(0,len(words)-1)

determined_word = words[word_selector]


l = 6 # that stands for user's number of chances that he/she can guess wrongly

print(f"word that you must guess made of {len(determined_word)} letters")

while True :

    user_guess = input("Take your guess :")

    if user_guess == determined_word:
        
        print("congrats")

        break



    elif user_guess in determined_word :

        detector_list = []

        for i in determined_word :
            
            if user_guess == i :

                detector_list.append(True)
            
            else:
                detector_list.append(False)
    
        k = 0

        for j in detector_list :

            k += 1 # this variable gives us an idea about position of the j

            if j == True :

                print(f"Letter {user_guess} appears in {k}-th position of the word.")
    


    else :

        l = l-1

        print(f"You have {l} right left to take a correct guess.")

        if l == 0 :

            print("The end,you failed.")

            break





