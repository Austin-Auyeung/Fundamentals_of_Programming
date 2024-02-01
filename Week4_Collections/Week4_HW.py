# 1. Access value 20 from the tuple. tuple1 = (“Car”, [34, 23, 8], False, [15, 20, 11])
tuple1 = ("Car", [34, 23, 8], False, [15, 20, 11])
print(tuple1[3][1])

#
print()
#

# 2. Slice the last 3 elements of the given list. List1 = [44, 12, 578, 21, 134, 67]
List1 = [44, 12, 578, 21, 134, 67]
print(List1[3:])

#
print()
#

# 3. Write a program to replace 20 with 200 in list1 = [5, 10, 15, 20, 75, 100, 50]. Try this approach:
# Use list1.index to get the position of 20. Then do list[position] = 200
list1 = [5, 10, 15, 20, 75, 100, 50]
index20 = list1.index(20)
list1[index20] = 200
print(list1)

#
print()
#

# 4. Change the value of 33 to 66 in the given tuple. tuple1 = (11, [64, 33], 243, 123)
tuple1 = (11, [64, 33], 243, 123)
indexList = tuple1.index([64, 33])
index33 = tuple1[indexList].index(33)
tuple1[indexList][index33] = 66
print(tuple1)

#
print()
#

# 5. Return a new set with unique items from both sets by removing duplicates.
# a. set1 = {10, 20, 30, 40, 50}                b. set2 = {30, 40, 50, 60, 70}
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
set3 = set1.union(set2)
print(set3)

#
print()
#
# 6. Create a new list by picking the odd-index items from the first list and even indexed items from the
# second list. list1 = [3, 6, 9, 12, 15, 18, 21], list2 = [4, 8, 12, 16, 20, 24, 28]
list1 = [3, 6, 9, 12, 15, 18, 21]
list2 = [4, 8, 12, 16, 20, 24, 28]
list3 = [list1[0::2], list2[1::2]]
print(list3)

#
print()
#

# 7. Consider list1 = [34, 54, 67, 89, 11, 43, 94]. Write a program to
# a. remove the item present at index 4
# b. add it to the 3rd position and at the end of the list.
list1 = [34, 54, 67, 89, 11, 43, 94]
# Slicing out the parts of the list without the number in the 4th index
list1First = list1[:4]
print(list1First)
list1Second = list1[4+1:]
print(list1Second)

# Appending the two parts of the list without the 4th index together
list1First.append(list1Second)
newList = list1First
print(newList)

# Assign the item taken out to the third position and last position
index4 = list1[4] # Assigning the taken out number to a variable
newList[3] = index4 # Changing the third position to the number taken out
newList.append(index4) # Appending the number taken out to the list to add it to the end
print(newList)
