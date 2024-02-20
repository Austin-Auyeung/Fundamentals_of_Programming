####################### Question 1: Write a program to print a list of all prime numbers till a given target number.
# target_number = int(input("Enter a number greater than 1: "))
#
# primeNum = []

# if target_number <= 1:
#     print("Enter a number > 1")
# elif target_number == 2:
#     primeNum.append(target_number)
# else:
#     for num in range(2, target_number):
#         isPrime = True
#         for i in range(2, num):
#             if num % i == 0:
#                 isPrime = False
#                 break
#         if isPrime is True:
#             primeNum.append(num)


# for num in range(2, target_number + 1):
#     for j in range(2, num):
#         if num % j == 0:
#             break
#     else:
#         primeNum.append(num)


# print(primeNum)


print()
##################### Question 2: Write a program to print a list of all even numbers till a given target number.
target_number = int(input("Enter a target number: "))

even_list = []

for i in range(0, target_number + 1): # from 0 - entered number + 1 to include the entered number
    if i % 2 == 0: # starting from 0 see if the number has a remainder when divided into 2 which decides if it is even or odd
        even_list.append(i)

print(even_list)


print()
##################### Question 3: Use a loop to display elements from a given list present at odd index positions.
# listLength = int(input("How long should the list be? "))
# list1 = []
# for i in range(1, listLength + 1):
#     listElement = int(input(f"Enter list element {i}: "))
#     list1.append(listElement)

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
oddIndexList = []
for i in range(0, len(list1)):
    if list1.index(list1[i]) % 2 != 0: # checking to see the index of the i is divided into 2 will be even or odd based on remainder
        oddIndexList.append(list1[i]) # if it is odd then add it to the list

print(oddIndexList)


print()
################### Question 4: Find the highest number from a given list of numbers using for loop. Do not use any in-built functions
list2 = [10, 24, 8, 187, 34, 100]

highestNum = 0
for i in range(0, len(list2)):
    for j in range(0, len(list2)): # the same postion will be kept for i in the list while j runs through each position to see if the number in that position is greater
        if list2[i] < list2[j]: # checks each index of the list to see if there is a number higher than the current i index of the list if there is not then the it will not fall into this if statement and the highest number will be found
            highestNum = list2[j]
            break # break out of second for loop if a new highest number is found compared to the i then continue to check if there are more higher numbers
            # using a break because we already know the list index of i is smaller than the list index of j so we need to break out of this loop and continue the loop with a changed i value
print(f"The highest number in the given list is {highestNum}.")