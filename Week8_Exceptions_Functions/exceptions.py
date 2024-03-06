## Exception/Error - unwanted scenario that disrupts the normal flow of your program
'''
## Normal Statements
a = 5
b = 0

try:
    # Critical Statement
    print(a/b) # syntactically correct but incorrect logic wise so the error would be thrown only when running the program
except Exception:
    print("Something went wrong")
print("End")
'''
'''
try:
    print("Connection opened")
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    result = a / b
except ZeroDivisionError as e:
    print("Something went wrong- ", e)
except ValueError as e:
    print("Something went wrong- ", e)
except Exception as e:
    print("Something went wrong- ", e)
else:
    print(result) # else block code would run only if there are no errors thrown from the try block

finally:
    print("Connections closed") # used for the code that needs to be executed of whether an error is thrown or not
print("End")
'''


numbers = [1, 2, 3, 4, 0, 5, 6]

for num in numbers:
    try:
        result = 10/num
    except ZeroDivisionError as e:
        print(e)
    except Exception as e:
        print(e)
    else:
        print(result)