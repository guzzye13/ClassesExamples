# INHERITANCE
# If the class you're writing is a specialized version of another class
# you wrote, you can use inheritance.
# The original class is called the parent class, and the new class is the child class.


class Car():  # Parent class must appear before the child class in the file.
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = '\n' + str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


class Battery():
    """A simple attempt to model a battery for an electric car."""
    def __init__(self, battery_size=70):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + " -kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)


class ElectricCar(Car):  # child class, name of the parent class must be included
    # in parentheses in the definition of the child class.
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):  # Takes in the information required to make a Car instance.
        """Initialize attributes of the parent class.
           Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)  # super() function a special function that helps python make
        # connections between parent and the child class. This line tells Python to call the __init__() method
        # from ElectricCar's parent class, which gives an ElectricCar instance all the attributes of its parent class.
        # super comes from calling the parent class a superclass and the child class a subclass.
        # DEFINING ATTRIBUTES AND METHODS FOR THE CHILD CLASS.
        self.battery = Battery()

    def describe_battery(self):  # add this method, prints information about the battery
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")


my_tesla = ElectricCar('tesla', 'model s', 2016)  # make an instance of the ElectricCar class, and store it in my_tesla
# This line calls the __init__() method defined in ElectricCar, which in turn tells python to call the __init__() method
# defined in the parent class Car.
# Provide 3 arguments
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
