########### Question 1
targetNumber = int(input("Enter a target number: "))
x = 0
while x <= targetNumber:
    if x % 2 != 0:
        print(x)
    x += 1


print()
########### Question 2
fruits_list = ["banana", "orange", "apple", "kiwi", "apple", "apple", "grapes"]
new_list = []

for str1 in fruits_list:
    if str1 != "apple":
        new_list.append(str1)

print(new_list)


print()
############ Question 3
import random
random = random.randint(1, 2)

play = "YES"

while play == "YES":
    choice = input("Pick heads or tails: ").lower()

    if random == 1:
        computer = "heads"
    else:
        computer = "tails"

    if choice == "heads" and computer == "tails":
        print(f"\nYou picked {choice}, the computer picked {computer} - You Win!")
    elif choice == "tails" and computer == "heads":
        print(f"\nYou picked {choice}, the computer picked {computer} - You Lose!")
    else:
        print(f"\nYou picked {choice}, the computer picked {computer} - You Tied!")

    play = input("\nWould you like to play again? YES or NO: ").upper()



print()
############ Question 4
list1 = [75, 150, 180, 145, 525, 50]

for num in list1:
    if num > 500:
        break
    elif num > 150:
        continue
    else:
        print(num)


print()
########## Question 5
rows = int(input("Enter the number of rows: "))

for i in range(1, rows + 1):
    for j in range(1, i + i, 2):
        print(j, end = " ")
    print()