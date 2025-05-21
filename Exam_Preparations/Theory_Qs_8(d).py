try:
    with open('x.txt',"r") as file:
        text=file.read()
except FileNotFoundError:
    print("File not found")