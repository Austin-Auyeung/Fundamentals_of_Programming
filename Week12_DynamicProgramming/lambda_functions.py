def square_num(a):
    return a * a


print(square_num(5))

square_num1 = lambda a: a * a
print(square_num1(5))

add_nums = lambda a, b: a + b
print(add_nums(4, 5))

hello_user = lambda name: f"Hello {name}!"
print(hello_user("John"))

# Write a lambda function that checks whether a number is even or odd
# Print "Even Number" if it is even otherwise print "Odd Number"
check_even = lambda num: "Even Number" if num % 2 == 0 else "Odd Number"
print(check_even(113293))

# Immediately Invoked Function Expressions or IIFE
print((lambda name: f"Hello {name}!")("Jane"))


print((lambda num: num + 5)(10))

# Higher Order Functions - filter, map, reduce
nums = [3, 2, 6, 8, 4, 6, 2, 9]


def is_even(n):
    return n % 2 == 0


even_nums = filter(is_even, nums)
print(list(even_nums))

even_nums1 = filter(lambda x: x % 2 == 0, nums)
print(list(even_nums1))


# Map --> Used to preform some operation on every element in a list
def double_num(n):
    return n * 2


doubles = map(double_num, nums)
print(list(doubles))

doubles1 = map(lambda n: n * 2, nums)
print(list(doubles1))

cities = ["New York", "Miami", "Phoenix", "Columbus", "Pittsburgh"]
# Using map and lambda, return a list with the lengths of all the cities
str_len = map(lambda l: len(l), cities)
print(list(str_len))


# Reduce --> to calculate a single value for a given list. Ex: sum, average etc..
from functools import reduce

def add_all(a, b):
    return a + b


total_sum = reduce(add_all, nums)
print(total_sum)

total_sum1 = reduce(lambda a, b: a + b, nums)
print(total_sum1)