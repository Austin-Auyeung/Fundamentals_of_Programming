'''
def sayHello(name):
    print(f"Hello {name}")

def userDetails():
    user_name = input("Enter a name: ")
    sayHello(user_name)
    user_city = input("Enter a city: ")
    print(f"You are from {user_city}")
userDetails()
'''


'''
##### RECUSRISON
def test1(n):
    if n > 0:
        print("Printing the value.")
        print(n)
        print("Calling the function.")
        test1(n-1)

test1(3)
print()

def test2(n):
    if n > 0:
        print("Calling the function.")
        test2(n - 1)
        print("Printing the value.")
        print(n)

test2(3)
'''

'''### Write a function to find the factorial of a number
def factorial(num):
    if num < 0:
        print("Please provide a positive number")
        return
    elif num <= 1:
        return 1
    else:
        return num * factorial(num - 1)


print(factorial(5))'''