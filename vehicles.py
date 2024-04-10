"""
Program: vehicles.py
Author: Tomi Simic
Last date modified: 2024-04-06
This program is to be used for Assignment M03 Lab - Case Study: Lists,
Functions, and Classes
"""
# pseudo code:
# create Vehicle class storing instance attributes
# create Automobile class that inherits from Vehicle class
# create funciton to gather user input
# main function that prompts and displays information


# Creating Vehicle class:
class Vehicle:
    """Stores vehicle type"""

    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type


# Creating Automobile class:
class Automobile(Vehicle):
    """Stores other attributes for the car"""

    def __init__(self, vehicle_type, year, make, model, trim, accessories):
        super().__init__(vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.trim = trim
        self.accessories = accessories

    def display(self):
        """Displays the results entered."""
        print("Vehicle type:", self.vehicle_type)
        print("Year:", self.year)
        print("Make:", self.make)
        print("Model:", self.model)
        print("Number of doors:", self.trim)
        print("Type of roof:", self.accessories)


# User input collection:
def user_input():
    """Gathers user information"""
    vehicle_type = input("Please enter the type of vehicle (i.e.: Car, Truck, \
plane, boat, or a broomstick): ")
    year = input("Please enter vehicle's year: ")
    make = input("Please enter vehicle's make: ")
    model = input("Please enter vehicle's model: ")
    trim = input("Please enter vehicle's number of doors: ")
    accessories = input("Please enter vehicle's root type: ")
    return vehicle_type, year, make, model, trim, accessories


# Main function:
if __name__ == "__main__":
    details = user_input()
    my_car = Automobile(*details)
    my_car.display()
