# Question 1 : Take an input string from the user and create a new string with the first, middle, and last
# characters of the input string
userStr = input("Enter a string: ")
firstLetter = userStr[0] # The first letter is always at the index of 0
middleIndex = int(len(userStr)/2) # The middle letter is found by getting the middle index of the string by dividing its length by 2 which will be half of the string
middleLetter = userStr[middleIndex]
lastLetter = userStr[-1] # The last letter is found by using the index of -1 (first letter starting at the end)

newStr = firstLetter + middleLetter + lastLetter

print(newStr)

# Question 2 : Take an input string from the user and create a new string made of the middle three
# characters of the input string
userStr1 = input("Enter a string: ")
middleIndex1 = int(len(userStr1)/2) # First finding the middle 
newStr1 = userStr1[middleIndex1 -1: middleIndex1 +2]

print(newStr1)