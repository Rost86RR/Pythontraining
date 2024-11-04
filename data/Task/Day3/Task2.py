import pandas as pd

data = pd.DataFrame({
    'product': ['Widget A', 'Widget B', 'Widget C', 'Widget D', None],
    'sales': [200, None, 300, 150, 100],
    'quantity': [10, None, 15, 7, None]
})

#select the rows where sales is greater than or equal to 150
sales_greater_equal_150 = data[data['sales'] >= 150]
print(sales_greater_equal_150)

#select lines where product is not equal to ‘Widget A’
not_Widgat_A = data[data['product'] != 'Widget A']
print(not_Widgat_A)