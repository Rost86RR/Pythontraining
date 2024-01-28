# Conditional statements: if, if..else, elif;

# Example 1: Print a person is eligible for vote or not
# Age >= 18

age = 19
if age >= 18:
    print("Eligible for vote")
else:
    print("Not eligible for vote")

# Example 2:------------------------------------------------------------------------------------

if True:
    print("true condition")
else:
    print("false condition")

# Example 3:------------------------------------------------------------------------------------

if 1:
    print("one")
else:
    print("not one")

# Example 4: Find a number is even/odd----------------------------------------------------------

num = 10
if num % 2 == 0:
    print("Given number is Even")
else:
    print("Given number is Odd")

# Example 5: if else in single line (ternary operator)-------------------------------------------

num = 11
print("Given number is Even") if num % 2 == 0 else print("Given number is Odd")

# Example 6: if else - multyple stetaments in single line----------------------------------------

a = 20
{print("hello"), print("python")} if a >= 10 else {print("hi "), print("java")}

# Example 7: multyple conditions using elif

weekno = 4

if weekno == 1:
    print("Sunday")
elif weekno == 2:
    print("Monday")
elif weekno == 3:
    print("Tuesday")
elif weekno == 4:
    print("Wednesday")
elif weekno == 5:
    print("Thursday")
elif weekno == 6:
    print("Friday")
elif weekno == 7:
    print("Saturday")
