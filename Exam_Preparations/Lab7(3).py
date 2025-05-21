import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("FuelConsumptionCo2.csv")

plt.figure(figsize=(10, 6))
plt.scatter(df['ENGINESIZE'],df['FUELCONSUMPTION_CITY'],color='blue',label='Fuel Consumption vs Engine Size')
plt.xlabel('Engine Size')
plt.ylabel('Fuel Consumption')
plt.legend()
plt.title('Fuel Consumption vs Engine Size')
plt.grid()
plt.show()