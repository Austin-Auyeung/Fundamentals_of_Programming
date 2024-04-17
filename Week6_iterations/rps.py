######### Question 2: Rock, Paper, Scissors
import random

# rand_num = random.random() # always returns a value between 0 and 1
# # print(round(rand_num, 2))
# random = random.randint(1, 100)
choice = "yes"
while choice.lower() == "yes":
    userMove = input("Pick your move - rock/paper/scissors: ")
    rand_num = round(random.random(), 2)
    compMove = ""
    if rand_num >= 0 and rand_num < 1/3:
        compMove = "rock"
    elif rand_num >= 1/3 and rand_num < 2/3:
        compMove = "paper"
    else:
        compMove = "scissors"

    result = ""
    if userMove == compMove:
        result = "Tie."
    elif userMove == "rock":
        if compMove == "paper":
            result = "You lose!"
        else:
            result = "You Win!"
    elif userMove == "scissors":
        if compMove == "paper":
            result = "You Win!"
        else:
            result = "You lose!"
    elif userMove == "paper":
        if compMove == "scissors":
            result = "You lose!"
        else:
            result = "You win!"

    print(f"You picked {userMove}. Computer picked {compMove}. {result}")
    choice = input("Would you like to play again? Yes or No: ")

print("Thank you!")