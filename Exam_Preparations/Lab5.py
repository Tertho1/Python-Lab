class Employee:
    def __init__(self,name,employee_id,salary,department):
        self.name=name
        self.employee_id=employee_id
        self.salary=salary
        self.department=department
    def display_employee_info(self):
        print(f"Name: {self.name}\nEmployee ID: {self.employee_id}\nSalary: {self.salary}\nDepartment: {self.department}")
class Manager(Employee):
    def __init__(self,name,employee_id,salary,department,team_size,team_members):
        super().__init__(name,employee_id,salary,department)
        self.team_members=team_members
        self.team_size=len(team_members)
    def display_employee_info(self):
        super().display_employee_info()
        print(f"Team Size: {self.team_size}")
        print(f"Team Members:{self.team_members}")
    def add_team_member(self,team_member):
        self.team_members.append(team_member)
        self.team_size=len(self.team_members)
    def remove_team_member(self,team_member):
        if team_member in self.team_members:
            self.team_members.remove(team_member)
            self.team_size=len(self.team_members)
        else:
            print(f"{team_member} not found in the team.")
    def update_salary(self,new_salary):
        self.salary=new_salary
        print(f"Salary updated to {self.salary}")
e1=Employee("John Doe",101,50000,"IT")
e1.display_employee_info()
m1=Manager("Jane Smith",102,70000,"HR",3,["Alice","Bob","Charlie"])
m1.display_employee_info()
m1.add_team_member("David")
m1.display_employee_info()
m1.remove_team_member("Alice")
m1.display_employee_info()
m1.update_salary(80000) 
m1.display_employee_info()  
    