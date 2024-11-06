import pandas as pd

# Первый DataFrame с информацией о продуктах
data1 = pd.DataFrame({
    'product_id': [1, 2, 3],
    'product_name': ['Widget A', 'Widget B', 'Widget C'],
    'price': [100, 200, 300]
})

# Второй DataFrame с информацией о продажах
data2 = pd.DataFrame({
    'product_id': [1, 2, 4],
    'quantity_sold': [10, 20, 15]
})

# Объединение по строкам
concat_rows = pd.concat([data1, data2], ignore_index=True)
print("\nОбъединение по строкам:")
print(concat_rows)

# Объединение по столбцам (axis=1)
concat_columns = pd.concat([data1, data2], axis=1)
print("\nОбъединение по столбцам:")
print(concat_columns)






