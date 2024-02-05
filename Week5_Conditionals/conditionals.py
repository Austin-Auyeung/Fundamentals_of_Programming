# If-else
'''
height = int(input("Enter your height in cms: "))
if height > 150:
    print("Can ride")
else:
    print("Can\'t ride")


### Nested if-else
height = int(input("Enter your height in cms: "))
if height > 120:
    print("Can ride")
    age = int(input("Enter your age: "))
    if age <= 18:
        print("Ticket is $7")
    else:
        print("Ticket is $12")
else:
    print("Can't ride")


### ###
height = int(input("Enter your height in cms: "))
total_bill = 0
if height > 120:
    print("Can ride")
    age = int(input("Enter your age: "))
    if age < 12:
        print("Ticket is $5")
        price = 5
    elif age >= 12 and age < 18:
        print("Ticket is $7")
        price = 7
    elif age >= 45 and age <= 55:
        print("Ticket is $0")
        price = 0
    else:
        print("Ticket is $12")
        price = 12
    photo = input("Do you want a photo taken? Enter Y/N: ").upper()
    if photo == "Y":
        total_bill = price + 3
        print(f"The total bill is {total_bill}")
    else:
        total_bill = price
        print(f"The total bill is {total_bill}")
else:
    print("Can't ride")
'''

### ###
k = True
while(k == True):
    grade = int(input("Enter your grade: "))
    if grade < 60:
        print("Your grade is F")
    elif grade < 70:
        if grade < 64:
            print("Your grade is D-")
        elif grade < 67:
            print("Your grade is D")
        else:
            print("Your grade is D+")
    elif grade < 80:
        if grade < 74:
            print("Your grade is C-")
        elif grade < 77:
            print("Your grade is C")
        else:
            print("Your grade is C+")
    elif grade < 90:
        if grade < 84:
            print("Your grade is B-")
        elif grade < 87:
            print("Your grade is B")
        else:
            print("Your grade is B+")
    else:
        if grade < 94:
            print("Your grade is A-")
        elif grade < 97:
            print("Your grade is A")
        else:
            print("Your grade is A+")
