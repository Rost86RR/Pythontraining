# Example 1: creating dictionary

mydic = {101:"x", 102:"y", 103:"z"}
print(mydic) # {101: 'x', 102: 'y', 103: 'z'}

# Example 2: accessing items from dictionary -----------------------------------------------------------

mydic2 = {
    "brand" : "Hundai",
    "model" : "i10",
    "year" : 2021
}

print(mydic2["brand"]) # Hundai
print(mydic2["model"]) # i10
print(mydic2["year"]) # 2021

# using get()

x = mydic2.get("brand")
print(x) # Hundai
print(mydic2.get("brand")) # Hundai

# Example 3: change items in dictionary ----------------------------------------------------------------

mydic3 = {
    "brand" : "Hundai",
    "model" : "i10",
    "year" : 2021
}

mydic3["year"] = 2024
print(mydic3) # {'brand': 'Hundai', 'model': 'i10', 'year': 2024}

# Example 4: reading items from dictionary using loop ----------------------------------------------------

mydic4 = {
    "brand" : "Hundai",
    "model" : "i10",
    "year" : 2021
}

for i in mydic4:
    print(i) # prints only keys from dictionary : brand model year

for i in mydic4:
    print(mydic4[i]) # prints only values from dictionary : Hundai i10 2021

for i in mydic4.values():
    print(i) # prints only values from dictionary : Hundai i10 2021

for x, y in mydic4.items():
    print(x, y)  # brand Hundai
                 # model i10
                 # year 2021

# Example 5: check a key is exists in the dictionary or not  ---------------------------------------------

mydic5 = {
    "brand" : "Hundai",
    "model" : "i10",
    "year" : 2021
}

if "model" in mydic5:
    print("exist")
else:
    print("not exist")

print("model" in mydic5) # True

# Example 6: find number of items in the dictionary  -----------------------------------------------------

mydic6 = {
    "brand" : "Hundai",
    "model" : "i10",
    "year" : 2021
}

print(len(mydic6)) # 3

# Example 7: adding items to the dictionary  -------------------------------------------------------------

mydic7 = {
    "brand" : "Hundai",
    "model" : "i10",
    "year" : 2021
}

mydic7["color"] = "red"
print(mydic7) # {'brand': 'Hundai', 'model': 'i10', 'year': 2021, 'color': 'red'}

# Example 8: remove items to the dictionary  -------------------------------------------------------------

mydic8 = {
    "brand" : "Hundai",
    "model" : "i10",
    "year" : 2021
}

mydic8.pop("year")
print(mydic8) # {'brand': 'Hundai', 'model': 'i10'}

del mydic8["model"]
print(mydic8) # {'brand': 'Hundai'}

#del mydic8 # or you can use mydic8.clear()
#print(mydic8) # NameError: name 'mydic8' is not defined. Did you mean: 'mydic'?

# Example 9: coping the dictionary  ----------------------------------------------------------------------

mydic9 = {
    "brand" : "Hundai",
    "model" : "i10",
    "year" : 2021
}

mydic10 = mydic9
print(mydic10)