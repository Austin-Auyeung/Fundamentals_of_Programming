# 1. Access value 20 from the tuple. tuple1 = (“Car”, [34, 23, 8], False, [15, 20, 11])
tuple1 = ("Car", [34, 23, 8], False, [15, 20, 11])
print(tuple1[3][1])

#
print()
#

# 2. Slice the last 3 elements of the given list. List1 = [44, 12, 578, 21, 134, 67]
List1 = [44, 12, 578, 21, 134, 67]
print(List1[3:]) # slicing out the list after index 3

#
print()
#

# 3. Write a program to replace 20 with 200 in list1 = [5, 10, 15, 20, 75, 100, 50]. Try this approach:
# Use list1.index to get the position of 20. Then do list[position] = 200
list1 = [5, 10, 15, 20, 75, 100, 50]
index20 = list1.index(20) # find the index where 20 is
list1[index20] = 200 # change the index where 20 was to the number 200
print(list1)

#
print()
#

# 4. Change the value of 33 to 66 in the given tuple. tuple1 = (11, [64, 33], 243, 123)
tuple1 = (11, [64, 33], 243, 123)
tuple1[1][1] = 66 # change the index where 33 is to 66
# indexList = tuple1.index([64, 33])
# index33 = tuple1[indexList].index(33)
# tuple1[indexList][index33] = 66
print(tuple1)

#
print()
#

# 5. Return a new set with unique items from both sets by removing duplicates.
# a. set1 = {10, 20, 30, 40, 50}                b. set2 = {30, 40, 50, 60, 70}
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
set3 = set1.union(set2) # a set does not allow duplicates so using union to add the two sets together will automatically get rid of duplicates
print(set3)

#
print()
#
# 6. Create a new list by picking the odd-index items from the first list and even indexed items from the
# second list. list1 = [3, 6, 9, 12, 15, 18, 21], list2 = [4, 8, 12, 16, 20, 24, 28]
list1 = [3, 6, 9, 12, 15, 18, 21]
list2 = [4, 8, 12, 16, 20, 24, 28]
list3 = list1[1::2] # store all the odd indices in a list by starting at index 1 to the end and skipping a letter(every 2nd index)
list4 = list2[0::2] # store all the even indices in a list by starting at 0 to the end and every 2nd index
list3.extend(list4) # combine the 2 lists together
new_list = list3
print(new_list)

#
print()
#

# 7. Consider list1 = [34, 54, 67, 89, 11, 43, 94]. Write a program to
# a. remove the item present at index 4
# b. add it to the 3rd position and at the end of the list.
list1 = [34, 54, 67, 89, 11, 43, 94]
# Slicing out the parts of the list without the number in the 4th index
list1First = list1[:4] # getting the beginning without the 4th index starting at the beginning and ending before the 4th index
print(list1First)
list1Second = list1[4+1:] # getting the end of the list without 4th index, starting at the index after the fourth to the end
print(list1Second)

# Combining the two parts of the list without the 4th index together
list1First.extend(list1Second)
newList = list1First
print(newList)

# Assign the item taken out to the third position and last position
index4 = list1[4] # Assigning the taken out number to a variable
listIndex1 = newList[:2] # storing the list before the third position
listIndex1.append(index4) # appending the taken out index to the end of index 1 list
assign3rdPos = listIndex1 # storing the new position 3 list
print(assign3rdPos)
assign3rdPos.extend(newList[2:]) # adding the rest of the list (after the 1st index in the old list) to the end of the 3rd position list
finalList = assign3rdPos
finalList.append(index4) # appending the taken out index to the end of the final list
print(finalList)

#
print()
#

# 8. Write a program to add item 7000 after 6000 in the following Python List
# i. list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
indexList6000 = list1[2][2] # find the position of the sublist where we want to add 7000

addItem = [7000] # create a list for the item we want to add
indexList6000.extend(addItem) # extend the sublist with the list that contains 7000
print(list1)

# list1[2][2] = indexList6000 # insert this new list into the index where the sublist was
# print(list1)

#
print()
#

# 9. Extend list1 by adding the sub list list2.
# a. list1 = [“a”, “b”, [“c”, [“d”, “e”, [“f”, “g”], “k”], “l”], “m”, “n”]
# b. list2 = [“h”, “i”, “j”]
list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
list2 = ["h", "i", "j"]
subListPos = list1[2][1][2] # find the position of the sublist
print(subListPos)
subListPos.extend(list2) # adding the second list to the end of the sublist
print(list1)

#
print()
#

# 10. Reverse the given tuple. Tuple1 = (40, 19, 234, 12, 10, 123)
Tuple1 = (40, 19, 234, 12, 10, 123)
Tuple1 = Tuple1[-1::-1] # starting from the end of the list to the beginning, 1 step to the left each time(reverse)
print(Tuple1)

#
print()
#

# 11. Print the value of key ‘history’ in the below dictionary
dict1 = {
    "course": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}

print(dict1["course"]["student"]["marks"]["history"]) # Finding the value by using the keys