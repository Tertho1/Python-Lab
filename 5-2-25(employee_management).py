class employee:
    def __init__(self, name, id, department, salary):
        self.name = name
        self.id = id
        self.department = department
        self.salary = salary
    def display_info(self):
        return f"Name: {self.name}, ID: {self.id}, Department: {self.department}, Salary: {self.salary}"
class manager(employee):
    def __init__(self, name, id, department, salary,team_size=0,team_members=[]):
        super().__init__(name, id, department, salary)
        self.team_size = team_size
        self.team_members = team_members
    def display_info(self):
        return f"{super().display_info()}, Team Size: {self.team_size}, Team Members: {self.team_members}"
    def add_member(self, member):
        self.team_members.append(member)
        self.team_size += 1
        return f"Added {member} to the team."
    def remove_member(self, member):
        self.team_members.remove(member)
        self.team_size -= 1
        return f"Removed {member} from the team."
    def update_salary(self, salary):
        self.salary = salary
        return f"Updated salary to {salary}."

emp = employee("Alice Johnson", "E123", "Finance", 50000)
print("Employee Information:")
print(emp.display_info())
print()

mgr = manager("Bob Smith", "M456", "Engineering", 80000, 1, ["Tertho Ghosh"])
print("Manager Information:")
print(mgr.display_info())
print()

print(mgr.add_member("Charlie Brown"))
print(mgr.add_member("David Green"))
print("Updated Manager Information:")
print(mgr.display_info())
print()

print(mgr.remove_member("Charlie Brown"))
print("Updated Manager Information:")
print(mgr.display_info())
print()

print(mgr.update_salary(85000))
print("Final Manager Information:")
print(mgr.display_info())
