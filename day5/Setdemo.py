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


