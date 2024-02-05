# A List is a collection which is ordered and changeable.
# In Python lists are written with square brackets [].
# List is mutable

# Example 1: how to create a list------------------------------------------------------------------------

myList1 = [10, 20, 30, 40, 50]
myList2 = ["cherry", "banana", "apple"]
myList3 = ["cherry", 10, "apple", 20]
myList = list()                        # empty list

print(myList1)
print(myList1[0])

# Example 2: accessing items from the list----------------------------------------------------------------

myList4 = ["apple", "banana", "cherry"]  # index starts from 0

print(myList4[0])
print(myList4[1])
print(myList4[2])
print(myList4[-1])
print(myList4[-2])
print(myList4[-3])

# Example 3: range of indexes------------------------------------------------------------------------------

myList5 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(myList5[2 : 5]) # ['cherry', 'orange', 'kiwi']
print(myList5[-4 : -1]) # ['orange', 'kiwi', 'melon']

# Example 4: change item value------------------------------------------------------------------------------

myList6 = ["apple", "banana", "cherry"]

print(myList6)                              # ['apple', 'banana', 'cherry']
myList6[0] = "orange"  # this will change the values based on index
print(myList6)                              # ['orange', 'banana', 'cherry']

# Example 5: read the list items using loop-------------------------------------------------------------------

myList7 = ["apple", "banana", "cherry"]

for i in myList7:
    print(i)

# Example 6: read the list items using loop-------------------------------------------------------------------

myList8 = ["apple", "banana", "cherry"]

if "apple" in myList8:
    print("yes, apple is present in the array")
else:
    print("no, apple is not present in the array")

# Example 7: list length---------------------------------------------------------------------------------------

myList9 = ["apple", "banana", "cherry"]

print(len(myList9))   #3

# Example 8: add items-----------------------------------------------------------------------------------------

myList10 = ["apple", "banana", "cherry"]

myList10.append("orange")    # add an item at the end of the list
print(myList10)              # ['apple', 'banana', 'cherry', 'orange']

myList10.insert(1, "kiwi")        # add an item anywhere
print(myList10)                                  # ['apple', 'kiwi', 'banana', 'cherry', 'orange']

# Example 9: remove the item from the list----------------------------------------------------------------------

myList11 = ["apple", "banana", "cherry"]

myList11.pop(0)
print(myList11) # ['banana', 'cherry']

del myList11[0]
print(myList11) # ['cherry']

myList11.clear() # clear all items
print(myList11)

# Example 10: copy the list------------------------------------------------------------------------------------
# list()
myList12 = ["apple", "banana", "cherry"]

myList13 = list(myList12)

print(myList12) # ['apple', 'banana', 'cherry']
print(myList13) # ['apple', 'banana', 'cherry']

# copy()
myList14 = ["apple", "banana", "cherry"]

myList15 = myList14.copy()

print(myList14) # ['apple', 'banana', 'cherry']
print(myList15) # ['apple', 'banana', 'cherry']

# Example 10: combine/join lists--------------------------------------------------------------------------------
# Using + operator

myList16 = ["a", "b", "c"]
myList17 = [1, 2, 3]
myList18 = myList16 + myList17
print(myList18)                    # ['a', 'b', 'c', 1, 2, 3]

# Using loop statement

myList19 = ["a", "b", "c"]
myList20 = [1, 2, 3]

for i in myList20:
    myList19.append(i)
print(myList19)                    # ['a', 'b', 'c', 1, 2, 3]

# Using extend()

myList21 = ["a", "b", "c"]
myList22 = [1, 2, 3]

myList21.extend(myList22)
print(myList21)                     # ['a', 'b', 'c', 1, 2, 3]






