# --- Assignment : My Custom Class ---
# I'll start with a general 'Vehicle' class. This will be the parent for the others.
class Vehicle:
    # This is the constructor. I need this so I can give each vehicle
    # its own brand, year, and color when I create it.
    def __init__(self, brand, year, color):
        self.brand = brand
        self.year = year
        self.color = color

    # I'll add a simple method to print out the vehicle's details.
    def display_info(self):
        print(f"This is a {self.year} {self.color} {self.brand}.")

    # This is for the second part of the assignment. I'll make a basic
    # 'move' method here that the other classes can change.
    def move(self):
        print("The vehicle starts to move.")


# Now for the inheritance part. I'll make a 'Car' class that gets all the stuff from 'Vehicle'.
class Car(Vehicle):
    # I'm giving Car its own constructor so I can add a detail only cars have.
    def __init__(self, brand, year, color, fuel_type):
        # I use super().__init__() to run the constructor from the parent (Vehicle) class.
        # This saves me from re-typing self.brand, self.year, etc.
        super().__init__(brand, year, color)
        self.fuel_type = fuel_type

    # --- Activity 2: Polymorphism Challenge ---
    # Here, I'm re-defining the 'move' method just for the Car.
    # It has the same name as the one in Vehicle, but does something different.
    def move(self):
        print(f"My {self.brand} is Driving down the road... 🚗")


# I'll make another class that inherits from Vehicle to really show polymorphism.
class Plane(Vehicle):
    # It gets its own constructor too.
    def __init__(self, brand, year, color, airline):
        super().__init__(brand, year, color)
        self.airline = airline
    
    # And its own 'move' method.
    def move(self):
        print(f"The {self.airline} {self.brand} is Flying through the sky... ✈️")


# --- Testing it all out ---

# First, I'll create a Car object.
my_car = Car("Honda", 2022, "Red", "Petrol")

# Then, I'll create a Plane object.
my_plane = Plane("Boeing 747", 2018, "White", "British Airways")

# Let's see if the info prints correctly.
print("--- Checking my objects ---\n")
my_car.display_info()
my_plane.display_info()

# Now for the main test – the polymorphism part.
# I'm calling the same '.move()' method on both, but I expect different results.
print("\n--- Testing the 'move' method ---\n")
my_car.move()  # This should print the "Driving" message.
my_plane.move() # This should print the "Flying" message.