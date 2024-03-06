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

def check_palindrome(given1):
    if given1 == given1[-1::-1]:
        return "Palindrome"
    else:
        return "Not Palindrome"


palindrome = check_palindrome("level")
print(palindrome)


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