############ LISTS #############
# 1. Allow duplicate data
# 2. Order is maintained
# 3. Allows heterogeneous data
list1 = [10, "test", False, 23.24]
print(list1)


### Length of the list
print(len(list1))
### Allows indexing and slicing
print(list1[2])
print(list1[1:4])
print(list[-2])
##### Can hold other lists too
list2 = [34, 54.76, "hi", ["Hello", 45, False]]
print(list2[3][1])

####### Creating an empty list
countries = []

## New elements can be added to a list using append, insert, or extend
countries.append("Canada")
countries.append("France")
countries.append("Germany")
countries.append("France")
print(countries)
#append always adds elements at the end of the list

countries.insert(2, "Mexico")
# Insert can be used to add an element at a particular location

countries2 = ["USA", "Iceland", "Denmark"]
countries.extend(countries2)
# extend is an inplace function so it changes the object internally but doesnt return anything
print(countries)
# print(countries.append(countries2))
countries.append(countries2)
print(countries)

countries.pop() # removes the last element
print(countries)

## SORT function
countries.sort()
print(countries)

countries.sort(reverse=True)
print(countries)

## Membership test
print("USA" in countries) # True

## List to string
countries_str = '-'.join(countries)
print(countries_str)
print(type(countries))
print(type(countries_str))

## String to list
countries3 = countries_str.split('-')
print(countries3)


############# TUPLES ####################
# 1. Cannot be modified i.e cannot update, add, or remove an element
tuple1 = (12, 243, 4125, 23) ## inches, cms
print(tuple1[2])
# tuple1[3] = 99999


############# SETS ##################
# 1. Sets do not allow duplicates
# 2. Order is not guaranteed
courses = {"English", "Networking", "History", "Programming", "History"}
print(courses)

### SET operations
courses1 = {"English", "Data Analytics", "Economics", "History"}
print(courses.union(courses1))
print(courses.intersection(courses1))
print(courses.difference(courses1))
print(courses1.difference(courses))