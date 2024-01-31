# Question 1 : Take an input string from the user and create a new string with the first, middle, and last characters of the input string
userStr = input("Enter a string: ")
print(userStr)
firstLetter = userStr[0] # The first letter is always at the index of 0
middleIndex = int(len(userStr)/2) # The middle letter is found by getting the middle index of the string by dividing its length by 2 which will be half of the string
middleLetter = userStr[middleIndex]
lastLetter = userStr[-1] # The last letter is found by using the index of -1 (first letter starting at the end)

newStr = firstLetter + middleLetter + lastLetter

print(newStr)


# Question 2 : Take an input string from the user and create a new string made of the middle three characters of the input string
userStr1 = input("Enter a string: ")
print(userStr1)
middleIndex1 = int(len(userStr1)/2) # First finding the middle index by dividing the length of the string by 2
newStr1 = userStr1[middleIndex1 -1: middleIndex1 +2] # Using string slicing to get the charcters after and before the middle letter, the letter before is the middle index -1 and for the letter after it will need to be +2 since the second value is not inclusive so it will need to be one more index.
print(newStr1)


# Question 3 : Take 2 strings as inputs from the user. Append the second string in the middle of the first string
str1 = input("Enter your first string: ")
print(str1)
str2 = input("Enter your second string: ")
print(str2)

midIndex1 = int(len(str1)/2)
print(midIndex1)
firstHalf = str1[0:midIndex1]
firstMiddle = firstHalf + str2
newStr1 = firstMiddle + str1[midIndex1:]
print(newStr1)


# Question 4 : Take a string from the user and reverse it
userInput = input("Enter a string: ")
print(userInput)
reverse = userInput[-1::-1]
print(reverse)


# Question 5 : Extract the amount from the below string.
# “The total value of the 10 products purchased along with the tax is $150”
str = "The total value of the 10 products purchased along with the tax is $150"
amount = str[-3:]
print(amount)

# Question 6 : Try to change the 4th character of a given string. Were you able to do it?
# str[3] = 'C'
# str = str[4].replace(str[4], 'r')
print(str)
# The string object does not support item assignment. Changing characters in a string is not possible

#############################################################################################################################

name = input("Enter your name: ")
last = input("Enter your last name: ")
age = input("Enter your age: ")
ssn = input("Enter your ssn: ")
height = input("Enter your height: ")
weight = input("Enter your weight: ")

print(f"Hello {name} {last}! Thank you for applying. Please find your details below.\nAge: {age}\nSSN: {ssn}\nHeight: {int(height) * 0.3937} inches\nWeight: {int(weight) * 0.453}")
