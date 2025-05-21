def car_info(manufacturer, model, **kwargs):
    dict = {
        "Manufacturer": manufacturer,
        "Model": model,
    }
    for key, value in kwargs.items():
        dict[key] = value
    return dict


car = car_info("Subaru", "Outback", Color="Blue", Price=30000)
for key, value in car.items():
    print(f"{key}: {value}")
