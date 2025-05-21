# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# p1=Person("Tertho",24)
# print(p1.name,p1.age)

# class Student:
#     def __init__(self, name, id):
#         self.name = name
#         self.student_id = id

#     def __str__(self):
#         return f"Student: {self.name}, ID: {self.student_id}"

# s1 = Student("Alice", 1001)
# print(s1)

import pandas as pd

# s = pd.Series(10)
# print(s)

x = ["a", "b", "c"]
# s = pd.Series(10, x)
# print(s)

# s = pd.Series(x, range(4))
# print(s)

# dc = {"a": 1, "b": 2, "c": 3}
# s=pd.Series(dc)
# s = pd.Series(dc,index=["a", "c"])
# s= pd.Series(dc,index=['hj'])
# s = pd.Series(dc)
# print(s[s > 1])
# print(s)
# print(s.shape)
# import matplotlib.pyplot as plt
# print(s.nbytes,s.ndim,s.hasnans)
# print(s.describe())
# print(s.value_counts())
# print(s.unique(),s.nunique())
# print(s.isnull(),s.notnull())
# print(s.plot())
# plt.show()

data={
    'a': [1, 2, 3],
    'b': [4,5,  6],
    'c': [7, 8, 9]
}
import pandas as pd
df=pd.DataFrame(data)
print(df.count())
print(df.fillna(0))
# print(df.mean(numeric_only=True))
# print(df.info())
# print(df.groupby('a').mean())
# print(df.groupby('a')['b'].mean())
# print(df.sum(numeric_only=True),df.sum(axis=1,numeric_only=True))
# print(df[['a','b']])
# print(df.loc[:,['a']])
# print(df.iloc[:,0])
# print(df.loc[df['b']>4])
# print(df.iloc[(df['b']>4).values])
# print(df[(df['b']>4) & (df['a']>2)])
# df.assign(d=[1,2,3])    
# df['e']=[1,2,3]
# df.insert(loc=3,column='f',value=[1,2,3])
# print(df.dtypes)
# df['a']=df['a'].astype(float)
# print(df.dtypes)
# for i in df:
#     print(df[i].mean())

# df["total"]=df.sum(axis=1,numeric_only=True)
# print(df)
# xd=df[df['total']==df['total'].max()]
# print(xd)

x=[200,300,400,100,150]
p=[a for a in x if a>=200]
print(p)
