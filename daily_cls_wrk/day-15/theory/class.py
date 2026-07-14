class Student:
    def __init__(self, name, roll):
        self.std_name = name
        self.std_roll = roll

    def display(self):
        return f"Name: {self.std_name}\nRoll no.: {self.std_roll}"
    

name = input("Enter your name: ")
roll = input("Enter your roll number: ")

std = Student(name, roll)

print(std.display()) #Student.display(std)
