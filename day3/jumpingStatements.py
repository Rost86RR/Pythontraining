# break continue

# break ------------------------------------------------------------------------------------------
for i in range(1, 10):
    if i == 5:
        break
    print(i)
print("the program exited!")

# continue ----------------------------------------------------------------------------------------

for i in range(1, 10):
    if i == 5 or i == 3 or i == 7: # 1 2 4 6 8 9 (3 , 5, 7 were skipped)
        continue
    print(i)
print("the program exited!")