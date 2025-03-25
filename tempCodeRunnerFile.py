import matplotlib.pyplot as plt
plt.scatter(sizes,prices,color='blue',label='Data points')
plt.plot(sizes,m*sizes+b,color='red',label='Regression line')
plt.xlabel('Sizes')
plt.ylabel('Prices')
plt.legend()
plt.show()