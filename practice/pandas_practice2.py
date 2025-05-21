import pandas as pd
import matplotlib.pyplot as plt

# s=pd.Series([10,20,30,40,50])
# print(s[0])
# print(s[:3])

# s1=pd.Series([10,20,30])
# s2=pd.Series([40,50,60])
# print(s1+s2)

# print(s[s>=30])

# s.plot(kind='bar')
# # plt.show()

# data={
#     "calories":[420,380,390],
#     "duration":[50,40,45]
# }
# df=pd.DataFrame(data)
# print(df)



data = {
    "Name": ["Tom", "Nick", "John", "Emma", "Liam"],
    "Math": [85,90,92,88,95],
    "Science":[88,85,90,92,86],
    "History":[75,8,85,None,90]
}

df = pd.DataFrame(data)
# print("Original DataFrame:")
# print(df)

# avg=df.mean(numeric_only=True)
# print(avg)
# df.loc[len(df)]=["Average"]+list(avg)
# print("After adding average:")
# print(df)

print(f"Shape: {df.shape}")
print(f"Columns: {df.columns}")
print(f"Data Types: {df.dtypes}")
print(df.values)
print(df.info())
print(df.count())
print(df.std(numeric_only=True))
print(df.dropna())
print(df.fillna(0))
print(df.sort_values(by="Math",ascending=False))
print(df.groupby("Name")['Science'].mean())
print(df.pivot_table(values='Math',index='Name',columns='Science',aggfunc='mean'))

data = {
    "Name": ["Tom", "Nick", "John", "Emma", "Liam", "Nick"],
    "Math": [85, 90, 92, 88, 95, 91],
    "Science": [88, 85, 90, 92, 86, 85],
    "History": [75, 8, 85, 45, 90, 12]
}

df = pd.DataFrame(data)

pivot_df = df.pivot_table(values='Math', index='Name', columns='Science', aggfunc='mean')
print(pivot_df)
print(df.sum(numeric_only=True))
print(df.sum(numeric_only=True, axis=1))
df_numeric = df.drop(columns=["Name"])  # Remove non-numeric columns
sqrt_df = df_numeric.map(lambda x: x**0.5)
print(sqrt_df)
