import pandas as pd

data = pd.DataFrame({
    'product': ['Widget A', 'Widget B', 'Widget A', 'Widget C', 'Widget B'],
    'region': ['North', 'South', 'East', 'North', 'South'],
    'sales': [200, 300, 150, 400, 100],
    'quantity': [10, 15, 8, 5, 12]
})

#Grouping the data by product and find the total sales for each product
group_by_product = data.groupby('product')['sales'].sum()
print(group_by_product)

#Grouping the data by region and calculate the average quantity value for each region
group_by_region = data.groupby('region')['quantity'].mean()
print(group_by_region)