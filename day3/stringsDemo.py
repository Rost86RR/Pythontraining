# Example 1: ways of creating string variable-------------------------------------------------

s1 = "welcom"
s2 = 'welcom'
s3 = str("welcom")
s4 = str('welcom')

# Example 2: ways of creating string variable-------------------------------------------------
# mutable - cannot change the value in the variable
# immutable - can change the value in the variable
# string is immutable
# if the value is changed after updating then it is immutable

str1 = "welcom"
print(id(str1)) # 3139486487520 - the id of the variable

str1 = str1 + " to python"
print(id(str1)) # 1835498813232 - updated id of the variable

# Example 3: + and * with srting --------------------------------------------------------------

str = "welcom"
print(str + " programming") # concatenation / joining
print(str * 3) # welcomwelcomwelcom - print 3 times

# Example 4: slicing []-------------------------------------------------------------------------
# starting index from 0

str = "welcom"
# w e l c o m
# 0 1 2 3 4 5

print(str[0:3]) # wel
print(str[1:3]) # el
print(str[2:4]) # lc
print(str[2:5]) # lco
print(str[2:6]) # lcom
print(str[:6]) # welcom
print(str[2:]) # lcom
print(str[1:-1]) # elco -last 1 char removed
print(str[1:-2]) # elc -last 2 char removed

# Example 5: ord() and chr() -------------------------------------------------------------------------

print(ord("A"))   # 65 -returns the ASCCI code of the character
print(chr(65))    # A  -returns the character represented by the ASCCI number

# Example 6: max(), min(), len() ---------------------------------------------------------------------

print(max("abcdefg")) # g
print(min("abcdefg")) # a
print(len("abcdefg")) # 7

# Example 7: in, not in - return true/false -----------------------------------------------------------

s = "welcome"
print("elcome" in s)    # True
print("lome" in s)      # False

print("elcome" not in s)    # False
print("lome" not in s)      # True

# Example 8: string comparison ------------------------------------------------------------------------

print("tim" == "tie")          # False
print("free" != "freedom")     # True
print("arrow" > "aron")        # True
print("right" >= "left")       # True
print("teeth" < "tee")         # False
print("yellow" <= "fellow")    # False
print("abc" > "")              # True

# Example 9: converting string ------------------------------------------------------------------------

s = "String in PITHON"

s1 = s.capitalize()
print(s1)                                  # String in pithon

s2 = s.title()
print(s2)                                  # String In Pithon

s3 = s.lower()
print(s3)                                  # string in pithon

s4 = s.upper()
print(s4)                                  # STRING IN PITHON

s5 = s.swapcase()
print(s5)                                  # sTRING IN pithon

s6 = s.replace("in", "on")
print(s6)                                  # Strong on PITHON

# Example 9: reverse a string --------------------------------------------------------------------------
# Method 1
s = "welcom"
rev_str = ""
for i in s:
    rev_str = i + rev_str
print("reversed string is: ", rev_str)     # reversed string is:  moclew

# Method 1

s = "welcom"
rev_str2 = s[::-1]
print(rev_str2)                            # moclew