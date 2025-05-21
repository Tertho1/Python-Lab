import numpy as np

unites_sold = np.array(
    [[50, 60], [45, 55], [60, 70], [65, 75], [80, 90], [85, 95], [90, 100]]
)
prices= np.array([15,20])

sm=np.sum(unites_sold, axis=0)
print(f"Total unit A sold: {sm[0]}")
print(f"Total unit B sold: {sm[1]}")
print(f"Unit A Total Revenue: {sm[0]*prices[0]}")
print(f"Unit B Total Revenue: {sm[1]*prices[1]}")
avg=np.mean(unites_sold, axis=0)
print(f"Average unit A sold: {avg[0]:.2f}")
print(f"Average unit B sold: {avg[1]:.2f}")
mx=np.max(unites_sold, axis=0)
print(f"Max unit A sold: {mx[0]}")
print(f"Max unit B sold: {mx[1]}")
amax=np.argmax(unites_sold, axis=0)
days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
print(f"Max unit A sold on: {days[amax[0]]}")
print(f"Max unit B sold on: {days[amax[1]]}")
print(f"Total Revenue: {np.sum(sm*prices,axis=0)}")



