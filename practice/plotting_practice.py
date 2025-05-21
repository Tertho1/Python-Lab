import matplotlib.pyplot as plt
# plt.plot([1,2,3],[4,5,6])
# plt.show()

import seaborn as sns
import matplotlib.pyplot as plt  # Import Matplotlib

# Histogram with KDE
# sns.histplot(data=[1, 2, 2, 3, 3, 3, 4], kde=True)
# plt.show()
# Boxen Plot
# sns.boxenplot(data=[[1, 2, 2, 3, 3, 3, 4],[2,3,4,6]])  # Boxen plot needs a nested list
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# Read CSV file using pandas
df = pd.read_csv('FuelConsumptionCo2.csv')
m,b=np.polyfit(df['FUELCONSUMPTION_COMB_MPG'], df['CO2EMISSIONS'], 1)
plt.plot(df['FUELCONSUMPTION_COMB_MPG'], m*df['FUELCONSUMPTION_COMB_MPG']+b,color='red',linestyle='--')
plt.scatter(df['FUELCONSUMPTION_COMB_MPG'], df['CO2EMISSIONS'],color='purple',marker='.')
plt.show()


# Create the lmplot
# sns.lmplot(x='FUELCONSUMPTION_COMB_MPG', y='CO2EMISSIONS',data=df,scatter_kws={'color':'green'},line_kws={'color':'red'})
# plt.show()
# Heatmap (Fixed: Using a 2D array)
# sns.heatmap(data=[[1, 2, 3], [4, 5, 6], [7, 8, 9]])  # Must be 2D
# import pandas as pd
# df = pd.DataFrame({
#     "A": [1, 4, 7],
#     "B": [2, 5, 8],
#     "C": [3, 6, 9]
# })
# sns.pairplot(df)  # requires pandas dataframe
# sns.violinplot(data=[1, 2, 2, 3, 3, 3, 4])

plt.show()

# import plotly.express as px

# data = {'x': [1, 2, 3], 'y': [4, 5, 6]}

# fig = px.scatter(data, x='x', y='y')

# fig.show()


# import numpy as np
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D  # Required for 3D plotting

# # Sample Data
# x = np.linspace(-5, 5, 100)  # X values
# y = np.sin(x)                # Y values
# z = np.cos(x)                # Z values

# # Create a figure
# fig = plt.figure()

# # Add a 3D subplot
# ax = fig.add_subplot(111, projection='3d')

# # Plot the data in 3D
# ax.plot(x, y, z)

# # Show the plot
# plt.show()
