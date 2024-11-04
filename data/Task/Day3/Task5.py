import pandas as pd

data = pd.DataFrame({
    'product': ['Widget A', 'Widget B', 'Widget A', 'Widget C', 'Widget B'],
    'region': ['North', 'South', 'East', 'North', 'South'],
    'sales': [200, 300, 150, 400, 100],
    'quantity': [10, 15, 8, 5, 12]
})

#Create a new sales_with_tax column where the 10% tax will be added to each sales value
data['sales_with_tax'] = data['sales'].apply(lambda x : x * 1.1)
print(data)

###The function that will categorise products into a new sales_category column: if sales is greater than 200,
#assign the category ‘High’, if less than or equal to 200 - ‘Low’. Apply this function using apply()

#The function that will categorise the products in the new sales_category column: if sales are greater than 200,
# assign the category ‘High’, if less than or equal to 200 - ‘Low’. Apply this function using the apply() function
def categorize_sales(sales):
    if sales > 200:
        return 'High'
    else:
        return 'Low'

# Apply the function to each sales value and save the result to a new sales_category column
data['sales_category'] = data['sales'].apply(categorize_sales)
print("\nДанные с категорией продаж:")
print(data)