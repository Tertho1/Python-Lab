x=input("Enter an integer : ")
try:
    x=int(x)
    if x%3==0 and x%5==0:
        print("FizzBuzz")
    elif x%3==0:
        print("Fizz")
    elif x%5==0:
        print("Buzz")
    else:
        print(x)
except ValueError:
    print("Invalid input. Please enter an integer.")