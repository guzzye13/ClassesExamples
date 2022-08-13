# CREATING AND USING A CLASS
class Dog():  # class called Dog, empty parenthesis because this class
    # is being created from scratch
    """A simple attempt to model a dog"""
    def __init__(self, name, age):  # __init__() method is a special method
        # Python runs automatically whenever we create a new instance based on the
        # Dog class. The underscores help prevent pythons default method names
        # from conflicting with your method names.
        """initialize, name and age attributes. """
        self.name = name  # any variable prefixed with self is available to every method
        # in the class, and we'll also be able to access these variables through any instance
        # created from the class.
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(self.name.title() + " rolled over!")


my_dog = Dog('willie', 6)  # Python to create a dog  named 'Willie' whose age is 6.
# When python reads this class it calls the __init__() method with the two arguments.

print("My dog's name is " + my_dog.name.title() + ".")  # To access the attributes of an instance
# you use dot notation.
# python finds the attribute name associated with my_dog.
# same attribute referred to as self.name in class Dog.
print("My dog is " + str(my_dog.age) + " years old.")  # same approach instead
# we convert int to str
my_dog.sit()   # CALLING METHOD

# CREATING MULTIPLE INSTANCES
# Second dog called your_dog
your_dog = Dog('lucy',4)
print("\nYour dog's name is " + your_dog.name.title() + ".")
print("Your dog is " + str(your_dog.age) + " years old.")
your_dog.sit()
