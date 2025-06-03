# Method Overloading Example

class Calculator:
    def add(self, a, b, c=0):
        return a + b + c

calc = Calculator()
print(calc.add(2, 3))      # Output: 5
print(calc.add(2, 3, 4))   # Output: 9