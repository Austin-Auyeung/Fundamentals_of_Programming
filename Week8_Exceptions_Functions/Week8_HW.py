'''Write a function to check whether a given string or number is palindrome or not'''
def check_palindrome(given1):
    if given1 == given1[-1::-1]:
        return "Palindrome"
    else:
        return "Not Palindrome"


palindrome = check_palindrome("level")
print(palindrome)



'''Write a function to check whether a given is string is anagram or not'''
def check_anagram(str1, str2):
    str1 = str(sorted(str1))
    print(str1)
    str2 = str(sorted(str2))
    if str1 == str2:
        return "Anagrams"
    else:
        return "Not Anagrams"

result = check_anagram("life", "file")
print(result)
result2 = check_anagram("listen", "silent")
print(result2)



'''Write a function to that takes user name, birth year, budget, price of the product as
inputs and performs the following operations.'''
def user_info(name, birth, budget, price):
    try:
        age = 2024 - int(birth)
        num_products = round(int(budget) / int(price))
    except ValueError as e:
        print("Incorrect data type-", e)
    except ZeroDivisionError as e:
        print("Cannot divide by zero-", e)
    except Exception as e:
        print("Something went wrong-", e)
    else:
        print(f"Hello {name}! You are {age} years old and you can buy {num_products} products.")
    finally:
        print("Thank You for Visiting")

user_info("Jane", 1960, 300, 23)



'''Write a program to check whether we can create a triangle or not'''
def is_triangle(side1, side2, side3):
    if side1 >= side2 + side3 or side2 >= side1 + side3 or side3 >= side1 + side2:
        return "No"
    else:
        return "Yes"


print(is_triangle(7, 10, 5))
print(is_triangle(30, 20, 24))
print(is_triangle(1, 1, 3))
print(is_triangle(6, 3, 2))