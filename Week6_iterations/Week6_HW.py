####################### Question 1: Write a program to print a list of all prime numbers till a given target number.
target_number = int(input("Enter a number greater than 1: "))

primeNum = []

# if target_number <= 1:
#     print("Enter a number > 1")
# elif target_number == 2:
#     primeNum.append(target_number)
# else:
#     for num in range(2, target_number):
#         isPrime = True
#         for i in range(2, num):
#             if num % 1 == 0:
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


print(primeNum)


print()
##################### Question 2: Write a program to print a list of all even numbers till a given target number.
target_number = int(input("Enter a target number: "))

even_list = []

for i in range(0, target_number + 1):
    if i % 2 == 0:
        even_list.append(i)

print(even_list)


print()
##################### Question 3: Use a loop to display elements from a given list present at odd index positions.
listLength = int(input("How long should the list be? "))
list1 = []
for i in range(1, listLength + 1):
    listElement = int(input(f"Enter list element {i}: "))
    list1.append(listElement)

oddIndexList = []
for i in range(0, len(list1)):
    if list1.index(list1[i]) % 2 != 0:
        oddIndexList.append(list1[i])

print(oddIndexList)


print()
################### Question 4: Find the highest number from a given list of numbers using for loop. Do not use any in-built functions
list2 = [10, 24, 8, 187, 34, 100]

highestNum = 0
for i in range(0, len(list2)):
    for j in range(0, len(list2)):
        if list2[i] < list2[j]:
            highestNum = list2[j]
            break

print(f"The highest number in the given list is {highestNum}.")