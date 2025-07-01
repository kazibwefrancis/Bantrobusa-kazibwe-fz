#-----------------------------Tenzi Car Motors Inventory System----------------------------------------------------------------------------------------

# List of cars always Available in the showroom at all times 
companystock_list = [
    "Toyota Prado",
    "Toyota Landcruiser",
    "Mercedes GLE",
    "Range Rover sport",
    "Range Rover Discovery",
    "BMW X5",
    "Audi R8",
    "Mitsubishi Pajero"
]

#-----------------------------------------view method---------------------------------------------------------------------------------------------------
def view_inventory():
    print("Enter 1 to see current Car stock available and enter anything else to cancel ")
    userinput = input("> ") 

    if userinput == "1":
        for car in companystock_list:
            print(car)    
    else:
        print("You cancelled.")

view_inventory()

print('')

#-------------------------enter method------------------------------------------------------------------------------------------------------------   
def enter_newcarstock():
    print("Enter new cars here:")

items = []
print("Hello, please enter new car stock here if any are delivered, press enter when done to complete ")

while True:
    entry = input("> ")
    if entry == "":
        break
    items.append(entry)
    print("  your stock items are:", items)

print("\nFinal stock list:", items)

print('')

#-----------------------------update method-----------------------------------------------------------------
def update_carstock():
    # update companystock_list with entered stock
    print("To see updated car list type 2")
    updated_carlist = companystock_list + items

    userinput1 = input(">")
    print('')

    if userinput1 == "2":
        for car2 in updated_carlist:
            print(car2)
    else:
        print("you opted out ")

update_carstock()

# Code written by BANTROBUSA KAZIBWE FZ 2300707416 23/u/07416/eve