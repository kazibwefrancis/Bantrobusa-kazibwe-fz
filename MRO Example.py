# MRO Example

class Printer:
    def start(self):
        print("Printer starting...")

class Scanner:
    def start(self):
        print("Scanner starting...")

class MultiFunctionDevice(Printer, Scanner):
    pass

mfd = MultiFunctionDevice()
mfd.start()  # Output: Printer starting...
print(MultiFunctionDevice.__mro__)
# Output: (<class '__main__.MultiFunctionDevice'>, <class '__main__.Printer'>, <class '__main__.Scanner'>, <class 'object'>)