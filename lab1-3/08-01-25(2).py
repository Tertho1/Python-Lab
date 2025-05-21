def inventory_manager(d):
    def update_item():
        i = input("Enter item name to update: ")
        p = float(input("Enter new price: "))
        d[i] = p

    def delete_item():
        i = input("Enter item name to delete: ")
        if i in d:
            d.pop(i, None)
        else:
            print("\nItem not found.")

    def print_items():
        print("\nCurrent Inventory:")
        for k, v in d.items():
            print(f"{k}: {v}")

    while True:
        print("\nOptions:")
        print("1. Update Price")
        print("2. Delete Item")
        print("3. Print All Items")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            update_item()
        elif choice == "2":
            delete_item()
        elif choice == "3":
            print_items()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Try again.")

    return d


inventory = {"apple": 12, "banana": 5, "cherry": 20}
inventory_manager(inventory)
