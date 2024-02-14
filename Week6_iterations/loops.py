######## While Loop
'''
x = 1
while x < 5: # loop variable - x
    print(x)
    x += 1



### Print the first 10 natural numbers
x = 0
while x <= 10:
    print(x)
    x += 1



### Break
# x = 1
# while x <= 10:
#     if x == 3:
#         break
#     print(x)
#     x += 1

## Continue
x = 1
while x <= 10:
    if x == 3:
        continue
    print(x)
    x += 1
'''


############# FOR Loops
'''
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in nums:
    print(num +10)
'''


### Range
'''
# range(starting value, ending value, step
for i in range(1, 10, 2): # range - starting value is always 0; ending value is not included
    print(i)
'''

### Find the sum of the first 100 natural numbers
'''
sum = 0

for i in range(6):
    print(sum)
    print(i)
    sum += i
print(sum)
'''


### Print Multiplication table
'''
userInput = int(input("Pick a number from 1 to 10: "))
for i in range(1, 11):
    print(f"{userInput} * {i} = {userInput * i}")
'''

### Nested Loops
'''
for num in [1, 2, 3]:
    for letter in 'abc':
        print(num, letter)
'''

# rows = int(input("Enter the number of rows: "))
# for i in range(1, rows + 1):
#     for j in range(1, i + 1):
#         print(j, end = ' ')
#     print()

rows = int(input("Enter the number of rows: "))
for i in range(0, rows):
    for j in range(rows - i, 0, -1):
        print(j, end = " ")
    print()