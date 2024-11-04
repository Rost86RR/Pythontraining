import pandas as pd

data = pd.DataFrame({
    'product': ['Widget A', 'Widget B', 'Widget C', 'Widget D', None],
    'sales': [200, None, 300, 150, 100],
    'quantity': [10, None, 15, 7, None]
})

#Look at the data and identify which columns have missing values
print(data)

#Delete the rows with missing values and output the result
data_no_na = data.dropna()
print('Data without rows with gaps')
print(data_no_na)

#Fill all missing values with 0 and output the result
data_filled = data.fillna(0)
print(data_filled)
