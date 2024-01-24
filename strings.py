#  Do not use reserved keywords for variable names
'''
print('Hello World')
print(help('keywords'))

# Try to avoid multiple variable declaration simultaneously
a = b = c = 10 # shortcut for below. Works but not recommended
a = 10
b = 10
c = 10

print(a,b,c)


# Statement vs Expression
x = 47  # Statement
y = x + 10  # Expression


# Type Conversion --> to change the data type of a variable
# Convert floats and numeric strings to int
print(int("20"))
# print(int("20.24"))  # Errors out because int expects only whole number inside quotes

print(type(int("20")))

print(int(float("20.24")))


## STRINGS ##
# 3 ways to create a string - using single, double, or triple quotes
first_name = 'Jane'
last_name = "Doe"
address = "10 Main St."

job = "Physicians Assistant"  # Recommended to use double quotes for strings

## STRING FUNCTIONS
# len() --> returns the number of characters in a string
print(len("Hello"))

# upper and lower --> convert the string to appropriate case
print("Hello".upper())

# String Concatenation - adding up strings
first_name  = "Jane"
last_name = "Doe"
print(first_name + ' ' + last_name)

age = 24

print(first_name + ' ' + last_name + ": " + str(age))

# String Multiplication - can multiply a string with an int
print("Hello"*3)

# Accessing String Characters - a string is just a sequence of characters
name = "Jane Doe"
print(name[2])
print(name[8])  # throws index out of bound error
'''

name = "Jane Doe"
# Retrieving the Character at a given index
print(name.index('o'))  # returns 6
print(name.index('e'))  # returns the index of the first


