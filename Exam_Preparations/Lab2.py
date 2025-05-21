dict = {"Eggs": 50, "Potato": 20, "Milk": 100}
while True:
    print(
        """Select an option:
    1. Add item
    2. Remove item
    3. Print item
    4. Exit"""
    )
    option = int(input("Enter your option: "))
    if option == 1:
        item = input("Enter item name: ")
        price = int(input("Enter item price: "))
        dict[item] = price
        print(f"{item} added to the dictionary.")
    elif option == 2:
        item = input("Enter item name: ")
        if item in dict:
            del dict[item]
            print(f"{item} removed from the dictionary.")
        else:
            print("Item not found.")
    elif option == 3:
        for item, price in dict.items():
            print(f"{item}: {price}")
    elif option == 4:
        break
