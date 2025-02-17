import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_FILES = {
    "books": os.path.join(BASE_DIR, "books.json"),
    "customers": os.path.join(BASE_DIR, "customers.json"),
    "orders": os.path.join(BASE_DIR, "orders.json"),
}

def load_data(books, customers, orders):
    for key, file in DATA_FILES.items():
        try:
            with open(file, "r") as f:
                data = json.load(f)
            if key == "books":
                books.extend(data)
            elif key == "customers":
                customers.extend(data)
            elif key == "orders":
                orders.extend(data)
        except FileNotFoundError:
            print(f"File {file} not found. Skipping loading data.")
            
def save_data(books, customers, orders):
    for key, file in DATA_FILES.items():
        if key == "books":
            data = books
        elif key == "customers":
            data = customers
        elif key == "orders":
            data = orders
        with open(file, "w") as f:
            json.dump(data, f)
