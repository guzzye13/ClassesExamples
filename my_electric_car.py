from electric_car import ElectricCar
my_audi = ElectricCar('audi', 'model s', 2016)

print(my_audi.get_descriptive_name())
my_audi.battery.describe_battery()
my_audi.battery.get_range()