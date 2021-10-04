class Vehicle:
    # Class attribute
    color = "white"

    def __init__(self, name, max_speed, milage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = milage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"


v = Vehicle
print(v)


class Bus(Vehicle):
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity=50)


School_bus = Bus("School Volvo", 180, 12)
print(School_bus.seating_capacity())


class bus(Vehicle):
    pass


class car(Vehicle):
    pass

School_bus2 = bus("School Volvo", 180, 12)
print(School_bus2.color, School_bus2.name, "Speed:", School_bus2.max_speed, "Mileage:", School_bus2.mileage)

car = car("Audi Q5", 240, 18)
print(car.color, car.name, "Speed:", car.max_speed, "Mileage:", car.mileage)

class vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self): #note this is a class variable
        return self.capacity * 100

class bus(vehicle):
    pass

school_bus = bus("School Volvo", 12, 50)
print("Total Bus fare is:", school_bus.fare())

class vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self): #note this is a class variable
        return self.capacity * 100

class bus(vehicle):
    def fare(self): # as a separate variable
        amount = super().fare() #note the inheritence here
        amount += amount * 10 / 100
        return amount

school_bus = bus("School Volvo", 12, 50)
print("Total Bus fare is:", school_bus.fare())

print(type(School_bus2)) #check type
print(isinstance(School_bus2, Vehicle)) #check if inheritance is happening