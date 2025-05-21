import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import numpy as np

# Load the dataset

df = pd.read_csv("FuelConsumptionCo2.csv")
y = df["CO2EMISSIONS"]
x = df["FUELCONSUMPTION_CITY"]

x_tr, x_te, y_tr, y_te = train_test_split(x, y, test_size=0.2, random_state=42)

##one way to do it
m, b = np.polyfit(x_tr, y_tr, 1)
print("Slope: ", m)
print("Intercept: ", b)
y_pd = x_te * m + b
mse1 = mean_squared_error(y_te, y_pd)
print("Mean Squared Error: ", mse1)
# print("y_pred: ",y_pd)
plt.scatter(x_tr, y_tr, color="blue", label="Train Data")
plt.scatter(x_te, y_te, color="red", label="Test Data")
plt.plot(x_te, y_pd, color="green", label="Regression Line")
plt.xlabel("FUELCONSUMPTION_CITY")
plt.ylabel("CO2EMISSIONS")
plt.title("Fuel Consumption vs CO2 Emissions")
plt.legend()
plt.grid()
plt.show()


# print(x_tr)
# print(x_te)
# print(y_tr)
# print(y_te)

## another way to do it
# x_tr=x_tr.to_frame()
# x_tr.insert(0,'bias',1)
# x_te=x_te.to_frame()
# x_te.insert(0,'bias',1)
# x_tr=np.array(x_tr)
# x_te=np.array(x_te)


##another way to do it
x_tr = np.c_[np.ones((x_tr.shape[0], 1)), x_tr]
x_te = np.c_[np.ones((x_te.shape[0], 1)), x_te]
# print(x_tr)
# print(x_te)


theta = np.linalg.inv(x_tr.T @ x_tr) @ x_tr.T @ y_tr
b1, m1 = theta
print("Slope: ", m1)
print("Intercept: ", b1)
y_pred = x_te @ theta
mse = mean_squared_error(y_te, y_pred)
print("Mean Squared Error: ", mse)
plt.scatter(x_tr[:, 1], y_tr, color="blue", label="Train Data")
plt.scatter(x_te[:, 1], y_te, color="red", label="Test Data")
plt.plot(x_te[:, 1], y_pred, color="green", label="Regression Line")
plt.xlabel("FUELCONSUMPTION_CITY")
plt.ylabel("CO2EMISSIONS")
plt.title("Fuel Consumption vs CO2 Emissions")
plt.legend()
plt.grid()
plt.show()
