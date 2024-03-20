# Inheritance:
#              Inheritance is a mechanism that allows a class to inherit properties and behaviors from another class

# Single inheritance

class Father:
    def __init__(self):
        self.property = 100000

    def display_property(self):
        print(f"Property value: {self.property}")


class Son(Father):
    pass


S1 = Son()
S1.display_property()


# Output:
#       Property value: 100000

# Multiple Inheritance

class Father:
    def height(self):
        print("My height is 5'11, similar to dad ")


class Mother:
    def color(self):
        print('My color is brown, similar to mom')


class Son(Father, Mother):
    pass


S1 = Son()
S1.height()
S1.color()

# Output:
#       My height is 5'11, similar to dad
#       My color is brown, similar to mom

