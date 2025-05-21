import pandas as pd

temp_series = pd.Series(
    [98.6, 98.9, 100.2, 97.9, 98.6, 96.2, 95.23],
    index=["Sat", "Sun", "Mon", "Tue", "Wed", "Thu", "Fri"],
)
print("Temperature readings for the week:")
print(temp_series)

avg_temp = temp_series.mean()
print("\nAverage temperature for the week: {:.2f}°F".format(avg_temp))

print(f"\nTemperature on Monday: {temp_series['Mon']}°F")

print(f'Head:\n{temp_series.head()}')
print(f'Tail:\n{temp_series.tail(3)}')
print(f'Describe:\n{temp_series.describe()}')
print(f"Value Count:\n{temp_series.value_counts()}")
print(f"Unique Values:\n{temp_series.unique()}")
print(f"NUnique Values:\n{temp_series.nunique()}")
print(f"Sort Values:\n{temp_series.sort_values()}")
print(f"Sort Index:\n{temp_series.sort_index()}")

l1=pd.Series([10,20,None,30,40])
print(f"Null Values:\n{l1.isnull()}")
print(f"Not Null:\n{l1.notnull()}")
print(f"Fill Values:\n{l1.fillna(0)}")