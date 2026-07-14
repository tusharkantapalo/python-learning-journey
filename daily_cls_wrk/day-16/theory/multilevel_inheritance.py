class Persion:

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name
    
class Employee(Persion):

    def __init__(self, name, emp_id):
        super().__init__(name)
        self.emp_id = emp_id

    def get_emp_id(self):
        return self.emp_id

class Developer(Employee):
    def __init__(self, name, emp_id):
        super().__init__(name, emp_id)

    def show_work(self):
        return "I am working on hash table"
    
dev1 = Developer("Matt", "001")

res = dev1.get_emp_id()

print(res)