num1 = input("Enter first number:") #100
num2 = input("Enter second number:") #200

print(type(num1)) #str
print(type(num2)) #str

print(num1 + num2) # 100200 bcoz it's str

# Approach 1-----------------------------------------------------------------------------
num1 = int(input("Enter first number:")) #100
num2 = int(input("Enter second number:")) #200

print(type(num1)) #int
print(type(num2)) #int

print(num1 + num2) # 300 bcoz it's int

# Approach 2------------------------------------------------------------------------------
num1 = input("Enter first number:") #100
num2 = input("Enter second number:") #200
print(int(num1) + int(num2)) # 300

#Example with float------------------------------------------------------------------------
num1 = input("Enter first number:") #10.5
num2 = input("Enter second number:") #20.5
print(float(num1) + float(num2)) # 31.0