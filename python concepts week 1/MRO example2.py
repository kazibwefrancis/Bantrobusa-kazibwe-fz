class Employee:
    def __init__(self, name):
        self.name = name

    def get_role_description(self):
        return "Generic Employee"

class Manager(Employee):
    def get_role_description(self): 
        return "Manages a team and projects."

    def conduct_meeting(self):
        return f"{self.name} is conducting a meeting."

class Developer(Employee):
    def get_role_description(self):
        return "Writes and maintains code."

    def write_code(self):
        return f"{self.name} is writing code."

class TechLead(Manager, Developer): 
    def __init__(self, name, team_size):
        super().__init__(name) 
        self.team_size = team_size

    # TechLead does not define get_role_description, so MRO will be used.

    def assign_task(self):
        return f"{self.name} is assigning tasks to {self.team_size} developers."

# Create an instance
lead_developer = TechLead("Alice", 5)

# Call methods
print(f"Employee Name: {lead_developer.name}")
print(f"Role Description: {lead_developer.get_role_description()}") 
print(lead_developer.conduct_meeting())
print(lead_developer.write_code())
print(lead_developer.assign_task())

