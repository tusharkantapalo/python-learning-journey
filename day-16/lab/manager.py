'''
Create a parent class named Employee with attributes name and salary. 
Add a method called get_details) that returns a string with the employee's 
name and salary. Create a child class named Manager that inherits from 
Employee. Add a new attribute called department.Override the get_details) 
method in the Manager class so it includes the department in the returned 
string
'''


class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_details(self):
        return f"Emplyee name: {self.name}\nEmployee salary: {self.salary}"
    
class Manager(Employee):

    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def get_details(self):
        return f"Emplyee name: {self.name}\nEmployee salary: {self.salary}\nDepartment: {self.department}"
    
emp_name = input("Enter the Employee name: ")
emp_salary = int(input("Enter the salary: "))

emp_obj = Employee(emp_name, emp_salary)

print("Employee details: ")
res1 = emp_obj.get_details()
print(res1)

mngr_name = input("Enter the manager name: ")
mngr_salary = int(input("Enter the salary: "))
mngr_dep = input("Enter the department: ")

mngr_obj = Manager(mngr_name, mngr_salary, mngr_dep)

print("Manager details: ")
res2 = mngr_obj.get_details()
print(res2)
