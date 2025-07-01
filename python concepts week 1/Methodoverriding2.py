class Animal:
    def speak(self):
        return "Animal sound"

class Dog(Animal):
    def speak(self): # Overrides Animal's speak method
        return "Woof"

class Cat(Animal):
    def speak(self): # Overrides Animal's speak method
        return "Meow"

# Create instances
generic_animal = Animal()
my_dog = Dog()
my_cat = Cat()

# Call the speak method
print(f"Generic Animal says: {generic_animal.speak()}")
print(f"Dog says: {my_dog.speak()}")
print(f"Cat says: {my_cat.speak()}")
