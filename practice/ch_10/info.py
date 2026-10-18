class Programmer:
    comp = "Microsoft"
    
    def greet(self):
        print(f"Good Morning! {self.name}")

    def getSal(self):
        return 100000


ob1 = Programmer()
ob1.name = input("Enter your name: ")
ob1.greet()
res = ob1.getSal()

print(res)
