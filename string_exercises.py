word = input("Enter a string: ")
print(word)

first = word[0]
last = word[-1]

str_length = len(word)
mid_index = int(str_length / 2)
print(mid_index)

middle = word[mid_index]

new_str = first + middle + last
print(new_str)


