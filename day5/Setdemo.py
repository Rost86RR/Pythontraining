# Example 1: creating a set

myset1 = {"apple", "banana", "cherry"}
print(myset1) # {'banana', 'apple', 'cherry'}

# Example 2: accessing items from a set ------------------------------------------------------------------

myset2 = {"apple", "banana", "cherry"}
for i in myset2:
    print(i)   # apple, banana, cherry

# Example 3: value exists in a set or not -----------------------------------------------------------------

myset3 = {"apple", "banana", "cherry"}
print("banana" in myset3)  # True
print("grape" in myset3)  # False

# Example 4: adding items to a set ------------------------------------------------------------------------
# add() - add single item; update() - add multiple items
myset4 = {"apple", "banana", "cherry"}
myset4.add("orange")
print(myset4) # {'orange', 'cherry', 'apple', 'banana'}
myset4.update(["mango", "grape"])
print(myset4) # {'mango', 'apple', 'banana', 'grape', 'orange', 'cherry'}

# Example 5: find number of items in a set - len()----------------------------------------------------------

myset5 = {"apple", "banana", "cherry"}
print(len(myset5)) # 3

# Example 6: remove items from a set - remove(); discard()--------------------------------------------------

myset6 = {"apple", "banana", "cherry"}
myset6.remove("banana")
print(myset6) # {'apple', 'cherry'}
#myset6.remove("abc") # KeyError: 'abc'
myset6.discard("apple")
print(myset6) # {'cherry'}
myset6.discard("abc")
print(myset6) # {'cherry'} # will not throw any error

# Example 7: clear all items from a set - clear() ---------------------------------------------------------

myset7 = {"apple", "banana", "cherry"}
myset7.clear()
print(myset7) # set()

del myset7
#print(myset7) # NameError: name 'myset7' is not defined. Did you mean: 'myset1'?

# Example 8: joining two sets - union() --------------------------------------------------------------------

set8 = {"a", "b", "c"}
set9 = {1, 2, 3}
set10 = set8.union(set9)
print(set10) # {'a', 1, 2, 'b', 3, 'c'}

# update()

set11 = {"a", "b", "c"}
set12 = {1, 2, 3}
set11.update(set12)
print(set11) # {'c', 1, 2, 3, 'b', 'a'}