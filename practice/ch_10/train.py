class Train:

    seat = 500
    price = 4

    @staticmethod
    def greet():
        print("Hello")

    def bookTicket(self, name, age, dist, seats):
        self.name = name
        self.age = age
        self.dist = dist
        Train.seat = Train.seat - seats

    def getInfo(self):
        if(self.seats < Train.seat):
            print(f"{self.name}'s ticket is confirmed.\nFare = {self.dist * Train.price * self.seats}")
        else:
            print("Seats are not available.")


ob1 = Train()
ob1.greet()

ob1.name = input("Enter your name: ")
ob1.age = int(input("Enter your age: "))
ob1.dist = int(input("Enter the distance: "))
ob1.seats = int(input("Enter the number of persons: "))

ob1.bookTicket(ob1.name, ob1.age, ob1.dist, ob1.seats)
ob1.getInfo()
