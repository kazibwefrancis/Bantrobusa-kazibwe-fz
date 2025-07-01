# Method Overriding Example

class Vehicle:
    def start(self):
        print("Starting vehicle...")

class Car(Vehicle):
    def start(self):
        print("Starting car with key...")

v = Vehicle()
v.start()  # Output: Starting vehicle...

c = Car()
c.start()  # Output: Starting car with key...