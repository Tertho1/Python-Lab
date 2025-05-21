def Dict_operations(dict):
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


dict = {"Eggs": 50, "Potato": 20, "Milk": 100}
Dict_operations(dict)


########################### Alternate Version ############################

# def items_list(dict):
#     while True:
#         print(""" Options:
#         update:Update the items_list
#         delete:delete an items to the items_list
#         print:print the items_list
#         exit:exit the program

#         """)
#         op=input("Select an operation:")
#         if op=="update":
#             item=input("enter an item: ")
#             price=int(input("enter price: "))
#             dict[item]=price
#             print(f"{item} added successfully")
#         elif op=="delete":
#             item=input("print enter an item which you want to delete:")
#             del dict[item]
#             print(f"{item}deleted successfully")
#         elif op=="print":
#             for key,value in dict.items():
#                 print(f"{key}:{value}")
#         elif op=="exit":
#             break
#         else:
#             print("Invalid input")

# dict={"soap":100,"mango":500,"oil":400,"pen":10}
# items_list(dict)
