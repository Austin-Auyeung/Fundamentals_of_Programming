import random

letters = list("abcdefghijklmnopqrstuvwxyz")
digits = list("0123456789")
symbols = list("!@#$%^&*()")

num_letters = int(input("How many letters do you want? "))
num_digits = int(input("How many digits do you want? "))
num_symbols = int(input("How many symbols do you want? "))

password_chars = []

for letter in range(0, num_letters):
    password_chars.append(random.choice(letters))

for digit in range(0, num_digits):
    password_chars.append(random.choice(digits))

for symbol in range(0, num_symbols):
    password_chars.append(random.choice(symbols))

print(password_chars)
random.shuffle(password_chars)
print(password_chars)

newPass = "".join(password_chars)
print(newPass)