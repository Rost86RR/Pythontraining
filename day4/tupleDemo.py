# A Tuple is a collection which is ordered and unchangeable.
# In Python tuples are written with round brackets ().
# Tuple is Immutable

# Example 1: how to create a tuple------------------------------------------------------------------------

myTuple = ("apple", "banana", "cherry")
print(myTuple)

# Example 2: access tuple items----------------------------------------------------------------------------

myTuple1 = ("apple", "banana", "cherry")
print(myTuple1[0])  # apple
print(myTuple1[-1]) # cherry

# Example 3: range of indexes------------------------------------------------------------------------------

myTuple2 = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(myTuple2[2 : 5])  # ('cherry', 'orange', 'kiwi')

# Example 4: changing tuple items---------------------------------------------------------------------------

# By default:
# 1) we cannot modify existing value
# 2) we cannot append a new value
# 3) we cannot insert a new value
# 4) we cannot remove a value

# but there is work around
# tuple --> list(modify) --> tuple

myTuple2 = ("apple", "banana", "cherry")
myList = list(myTuple2)
myList[0] = "orange"
myTuple2 = tuple(myList)
print(myTuple2)                    # ('orange', 'banana', 'cherry')




