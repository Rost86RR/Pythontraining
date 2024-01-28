# name = 'John'
# age = 37
# salary = 5000.50
name, age, salary = 'John', 37, 5000.50

# Approach 1
# print(name)
# print(age)
# print(salary)
print(name, age, salary)

# Approach 2
print("Name is:",name) # "," instead of "+"
print("Age is:",age)
print("Salary is:",salary)

# Approach 3
print("Name is:%s Age is:%d Salary is:%g" %(name, age, salary))

# Approach 4 {}
print("Name is:{} Age is:{} Salary is:{}" .format(name, age, salary))
