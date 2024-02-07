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

num = int(input("Enter a digit between 0 and 9: "))

print(dict1[num])

## Method 2: Using a list
list1 = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

num = int(input("Enter a digit between 0 and 9: "))

print(list1[num])
'''


######### Question 2: Rock, Paper, Scissors
import random

# rand_num = random.random() # always returns a value between 0 and 1
# # print(round(rand_num, 2))

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

