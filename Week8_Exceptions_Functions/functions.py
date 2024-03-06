'''Functions - reusable blocks of code'''

# Write a function to check whether a number is even or not
# num -> function parameter
'''
def checkEven(num):
    result = ""
    if num % 2 == 0:
        result = True
    else:
        result = False
    return result


### Making a function call
print(checkEven(5)) # 4 -> function argument
checkEven(2)

isEven = checkEven(384343)
print(isEven)

print("Hello") # does not have any return type
import random
randNum = random.random() # returns a number
'''