# WORK WITH CLASSES AND INSTANCES
"""A class that can be used to represent a car."""
class Car():
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):  # We define the __init__() method
        # with the self parameter.
        # init method takes three parameters and stores them in the attributes that
        # will be associated with instances made from this class.
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        # SETTING A DEFAULT VALUE FOR AN ATTRIBUTE
        self.odometer_reading = 0  # we create a new attribute
        # and set its initial value to 0.

    def get_descriptive_name(self):  # put's a car's year, make, and model into one string
        # describing the car.
        """Return a neatly formatted descriptive name."""
        long_name = '\n' + str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):  # makes it easy to read a car's mileage.
        """Print a statement showing the car's mileage."""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):  # takes in a mileage value and stores it in
        # self.odometer_reading.
        """Set the odometer reading to the given value.
           Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer.")

    def increment_odometer(self, miles):  # INCREMENTING AN ATTRIBUTES VALUES THROUGH A MODEL
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles


my_used_car = Car('subaru', 'outback', 2013)
print(my_used_car.get_descriptive_name())

# increment_odometer() and add to the mileage.
my_used_car.update_odometer(23500)
my_used_car.read_odometer()
my_used_car.increment_odometer(1000)
my_used_car.read_odometer()


my_new_car = Car('audi', 'a4', 2016)  # We make an instance from the Car class and store it in the variable
# my_new_car
print(my_new_car.get_descriptive_name())

# MODIFYING AN ATTRIBUTES VALUE DIRECTLY
my_new_car.odometer_reading = 23  # use dot notation to access the car's
# odometer_reading attribute and set its value directly.
my_new_car.read_odometer()


# MODIFYING AN ATTRIBUTE'S VALUE THROUGH A METHOD
my_new_car.update_odometer(443)  # call update_odometer() and give it 23 as an argument.
my_new_car.read_odometer()