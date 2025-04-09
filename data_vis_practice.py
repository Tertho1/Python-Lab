import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

# data = [1, 2, 3, 4, 5, 6]  
# plt.hist(data, bins=3, color='blue', edgecolor='black')  
# plt.title("Histogram Example")
# plt.xlabel("Values")
# plt.ylabel("Frequency")
# plt.show()

# data=np.random.normal(0,1,1000)
# print(data)
# plt.hist(data,bins=100,color='blue',edgecolor='black')
# plt.show()

# data=np.random.rand(10,5)
# sns.heatmap(data,annot=True,cmap='plasma')
# # print(data)
# plt.show()

# data=np.random.rand(10,5)
# df=pd.DataFrame(data,columns=['A','B','C','D','E'])
# sns.pairplot(df)
# plt.show()

# import plotly.express as px
# df = pd.DataFrame({'x': [1, 2, 3, 4, 5], 'y': [10, 20, 25, 30, 40]})
# fig = px.line(df, x='x', y='y', title='Line Chart Example')
# fig.show()

import altair as alt
import pandas as pd
# Data
data = {'Category': ['A', 'B', 'C', 'D'], 'Values': [10, 20, 15, 25]}
df = pd.DataFrame(data)
# Create bar chart
chart = alt.Chart(df).mark_bar().encode(
    x='Category',
    y='Values'
).properties(title="Bar Chart Example")
chart.show()

