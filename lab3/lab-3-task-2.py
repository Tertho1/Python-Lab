def make_car(manufacturer, model, **args):
    car = {"manufacturer": manufacturer, "model": model}
    car.update(args)
    return car


car = make_car("Subaru", "Outback", color="blue", tow_package=True)

print(car)
car = make_car("Subaru", "Outback", color="red", tow_package=True, ac=True)

print(car)
