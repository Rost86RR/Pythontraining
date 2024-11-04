import pandas as pd

data = pd.DataFrame({
    'product': ['Widget A', 'Widget B', 'Widget C', 'Widget D', None],
    'sales': [200, None, 300, 150, 100],
    'quantity': [10, None, 15, 7, None]
})

#Sorting the rows by sales column in ascending order
sorted_by_sales = data.sort_values(by = 'sales', ascending=True)
print(sorted_by_sales)

#Sorting the rows by quantity column in descending order
sorted_by_quantity = data.sort_values(by = 'quantity', ascending=False)
print(sorted_by_quantity)