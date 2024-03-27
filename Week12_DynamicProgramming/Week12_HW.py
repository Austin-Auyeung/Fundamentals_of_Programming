# Write a lambda function that takes 2 arguments and returns the product of those 2
# arguments
product = lambda a, b: a * b
print(product(10, 10))


# Write a lambda IIFE that takes 2 numbers as parameters and returns the difference
# between them.
print((lambda a, b: a * b)(10, 10))


# Using filter and lambda write a function that returns all the numbers greater than 5
# from a given list.
nums = [3, 2, 6, 8, 4, 6, 2, 9]
greater_five = list(filter(lambda n: n > 5, nums))
print(greater_five)


# Write a lambda function that returns num/5 if a given number is greater than 10.
# Otherwise, returns num + 5
greater_or = lambda n: n/5 if n > 10 else n + 5
print(greater_or(5))
print(greater_or(11))


# Using map and lambda, write a function to multiply every number in a list by 2.
multiply_two = list(map(lambda n: n * 2, nums))
print(multiply_two)


# Using map, filter and reduce
# i) Find the odd numbers from a given list
# ii) Square each odd number
# iii) Sum of squared odd numbers
