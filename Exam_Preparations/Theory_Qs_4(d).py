import pandas as pd

data = {
    "Name": ["Sweety", "Sweety", "Sweety", "Sweety"],
    "Math": [85, 92, 78, 90],
    "Science": [88, 95, 80, 85],
}
df=pd.DataFrame(data)
# print(df)
print(df['Math'].mean())
print(df['Science'].sum())
print(df.sort_values(by='Science'))
print(df['Science'].min())
print(df['Science'].max())
print(df.sum(numeric_only=True))

df['English'] = [90, 85, 88, 92]
print(df)

df.insert(2, 'History', [80, 85, 90, 95])
print(df)

df=df.assign(Geography=[75, 80, 85, 90])
print(df)