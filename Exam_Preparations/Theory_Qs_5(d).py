import random

lst=[1,2,3,4,5,6,7,8,9,10,'a','b','c','d','e']
elements=random.sample(lst,4)
ticket="".join(str(elem) for elem in elements)
print(f"Your winning ticket is: {ticket}")
