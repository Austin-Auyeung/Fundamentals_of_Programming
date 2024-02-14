######## Question 1 : Write a program that takes a digit as an input and returns the corresponding word.
# Example: Input is 1 and program returns “one”

## Method 1: Using a dictionary
'''# creating a mapping using dictionary with digit keys corresponding to their numbers
dict1 = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine"
}
# printing the string that corresponds to the id based on users number
num = int(input("Enter a digit between 0 and 9: "))

print(dict1[num])

## Method 2: Using a list
list1 = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

num = int(input("Enter a digit between 0 and 9: "))

print(list1[num])
'''

print()
######### Question 2: Rock, Paper, Scissors
import random

# rand_num = random.random() # always returns a value between 0 and 1
# # print(round(rand_num, 2))

userMove = input("Pick your move - rock/paper/scissors: ")
rand_num = round(random.random(), 2)
compMove = ""
# using a randomizer to pick for the computer
if rand_num >= 0 and rand_num < 1/3:
    compMove = "rock"
elif rand_num >= 1/3 and rand_num < 2/3:
    compMove = "paper"
else:
    compMove = "scissors"

result = ""
if userMove == compMove:  # deciding who wins based on the computers pick and user pick
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

print()
######### Question 3: Write a program that takes year as input and checks whether the given year is leap or not.
year = int(input("Enter a year: "))
leapYear = ""
if year % 4 == 0: # if the entered year is divisible by 4 it will fall into next if
    if year % 100 == 0: # if the year is divisible by 100 it will fall into next if. If not then it is not a leap year
        if year % 400 == 0: # The entered year is a leap year if its divisible by 400
            leapYear = "Leap Year"
        else:
            leapYear = "Non-leap Year" # the year is not a leap year if it not divisible by 400
    else:
        leapYear = "Leap Year" # if it is not divisible by 100 then the year is a leap year
else:
    leapYear = "Non-Leap Year" # if year is not divisible by 4 it will fall into this else

print(leapYear)

print()
######## Question 4: Write a program that simulates the logic shown in the below flowchart
print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
choice = input("Left or Right? ").upper()
# falls into each if based on the users choices
if choice == "LEFT":
    choice = input("Swim or Wait? ").upper()
    if choice == "WAIT":
        choice = input("Which door? Red, Blue, or Yellow: ").upper()
        if choice == "RED":
            print("You were burned by fire.\nGame Over!")
        elif choice == "BLUE":
            print("You were eaten by beasts.\nGame Over!")
        elif choice == "YELLOW":
            print("You Win!")
        else:
            print("Game Over!")
    else:
        print("You were attacked by a trout\nGame Over!")
else:
    print("You fell into a hole.\nGame Over!")