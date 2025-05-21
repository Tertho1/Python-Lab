import pandas as pd
data = {'Name': ['John', 'Emma', 'Ryan', 'Sophia', 'Liam'],
        'Age': [25, 30, 28, 35, 40],
        'Gender': ['M', 'F', 'M', 'F', 'M'],
        'Salary': [50000, 60000, 55000, 70000, 65000]}
df = pd.DataFrame(data)

print(df[["Name","Age"]])
sec_col=df.loc[:,['Name','Age']]
sec_col2=df.iloc[:,[0,1]]
print(sec_col)
print(sec_col2)

sec_row=df[df['Age']>30]
print(sec_row)

sec_row2=df.loc[df['Age']>30]
print(sec_row2)
sec_row3=df.iloc[(df['Age']>30).values]
print(sec_row3)

filtered=df[df['Age']>30]  
print(filtered)

filtered2=df[df['Gender']=='M']
print(filtered2)

df['Dept']=['Hr','Finance','IT','Admin','Marketing']
print(df)

df=df.assign(Experience=[3,5,7,8,6])
print(df)

df.insert(loc=4,column='Location',value=['New York','Chicago','Los Angeles','San Francisco','Boston'])
print(df)

df['Salary']=df['Salary'].astype(float)
print(df)

