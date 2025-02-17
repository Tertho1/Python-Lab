import tkinter as tk
from tkinter import messagebox

def inventory_manager_gui(d):
    def update_item():
        item = item_name_var.get()
        try:
            price = float(item_price_var.get())
            d[item] = price
            messagebox.showinfo("Success", f"Updated {item} to price {price}.")
            refresh_inventory()
        except ValueError:
            messagebox.showerror("Error", "Invalid price entered.")

    def delete_item():
        item = item_name_var.get()
        if item in d:
            del d[item]
            messagebox.showinfo("Success", f"Deleted {item} from inventory.")
            refresh_inventory()
        else:
            messagebox.showerror("Error", f"Item '{item}' not found.")

    def refresh_inventory():
        inventory_list.delete(0, tk.END)
        for k, v in d.items():
            inventory_list.insert(tk.END, f"{k}: {v}")

    # Create main window
    root = tk.Tk()
    root.title("Inventory Manager")

    # Labels and Entry Fields
    tk.Label(root, text="Item Name:").grid(row=0, column=0, padx=5, pady=5)
    item_name_var = tk.StringVar()
    item_name_entry = tk.Entry(root, textvariable=item_name_var)
    item_name_entry.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(root, text="Item Price:").grid(row=1, column=0, padx=5, pady=5)
    item_price_var = tk.StringVar()
    item_price_entry = tk.Entry(root, textvariable=item_price_var)
    item_price_entry.grid(row=1, column=1, padx=5, pady=5)

    # Buttons
    tk.Button(root, text="Update Price", command=update_item).grid(row=2, column=0, padx=5, pady=5)
    tk.Button(root, text="Delete Item", command=delete_item).grid(row=2, column=1, padx=5, pady=5)

    # Inventory List
    tk.Label(root, text="Current Inventory:").grid(row=3, column=0, columnspan=2, padx=5, pady=5)
    inventory_list = tk.Listbox(root, width=40, height=10)
    inventory_list.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

    refresh_inventory()

    # Run the GUI main loop
    root.mainloop()

# Example Inventory
demo_inventory = {"apple": 12, "banana": 5, "cherry": 20}
inventory_manager_gui(demo_inventory)
