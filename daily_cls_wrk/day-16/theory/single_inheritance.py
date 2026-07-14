class Employee: #it is the parent class

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

class Developer(Employee): #it is the child class

    def __init__(self, name):
        super().__init__(name)

dev1 = Developer("Matt")

res = dev1.get_name()

print(res)
