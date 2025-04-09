import numpy as np
# sizes=np.array([800,1200,1500,1000,1300])
# prices=np.array([150,220,300,180,250])

# mean_size=np.mean(sizes)
# mean_price=np.mean(prices)
# print(f"Mean size: {mean_size}\nMean price: {mean_price}")

# std_size=np.std(sizes)
# std_price=np.std(prices)
# print(f"Standard deviation of size: {std_size}\nStandard deviation of price: {std_price}")

# prob_above_200=sum(x>200 for x in prices)/len(prices)
# print(f"Probability of price above 200: {prob_above_200}")
# x=np.array(prices)>200
# print(x)
# print(f"Probability of price above 200: {np.mean(x)}")

sizes = np.array([800, 1200, 1500, 1000, 130])
prices = np.array([150, 220, 300, 180, 250])
# data_matrix = np.array([sizes, prices])
# print(data_matrix)
# colum_mat=np.column_stack((sizes,prices))
# print(colum_mat)
# row_mat=np.vstack((sizes,prices))
# print(row_mat)

m,b=np.polyfit(sizes,prices,1)
# print(f"Slope: {m:.3f}, Intercept: {b:.3f}")

# new_size=1100
# new_price=m*new_size+b
# print(f"Predicted price for size {new_size}: {new_price:.3f}")

import matplotlib.pyplot as plt
# plt.plot(sizes,prices,color='blue',label='Data points')
# plt.plot(sizes,m*sizes+b,color='red',label='Regression line')
# plt.xlabel('Sizes')
# plt.ylabel('Prices')
# plt.legend()
# plt.show()

x_range=np.linspace(800.00,1500.00,10)
y_range=m*x_range+b
plt.plot(x_range,y_range,color='green',label='Regression line')
plt.show()
print(x_range,y_range)
integral=np.trapezoid(y_range,x_range)
print(f"Integral of regression line: {integral:.3f}")

# x=sizes
# y=prices
# n=len(x)
# m=(n*np.sum(x*y)-np.sum(x)*np.sum(y))/(n*np.sum(x**2)-(np.sum(x))**2)
# c=(np.sum(y)-m*np.sum(x))/n
# print(f"Slope: {m:.3f}, Intercept: {c:.3f}")

# m_b, c_b=np.polyfit(x,y,1)
# print(f"Slope: {m_b:.3f}, Intercept: {c_b:.3f}")


# v=np.array([100,200,300,400,500])
# r=np.array([50,90,120,160,190])
# n=len(v)

# m_manual=(n*np.sum(v*r)-np.sum(v)*np.sum(r))/(n*np.sum(v**2)-(np.sum(v))**2)
# b_manual=(np.sum(r)-m_manual*np.sum(v))/n
# print(f"Slope: {m_manual:.3f}, Intercept: {b_manual:.3f}")

# m,b=np.polyfit(v,r,1)
# print(f"Slope Polyfit: {m:.3f}, Intercept: {b:.3f}")

# if m==m_manual and b==b_manual:
#     print("Verified")
# else:
#     print("Not verified")

# new_visitor=600
# new_revernue=m*new_visitor+b
# print(f"Predicted revenue for {new_visitor} visitors: {new_revernue:.3f}")

# plt.title("Visitors vs Revenew")
# plt.scatter(v,r,color='blue',label='Data points')
# plt.xlabel("visitors")
# plt.ylabel("revenue")
# plt.plot(v,m*v+b,color='red',label='Regression line')
# plt.scatter(new_visitor,new_revernue,color='green',label='Predicted revenue')
# plt.legend()
# plt.show()