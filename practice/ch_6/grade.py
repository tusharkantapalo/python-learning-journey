name = input("Enter your name: ")
m1 = int(input("Enter the mark of first subject: "))
m2 = int(input("Enter the mark of second subject: "))
m3 = int(input("Enter the mark of third subject: "))

avg = (m1 + m2 + m3) / 3

if (avg >= 40 and m1 >= 33 and m2 >= 33 and m3 >= 33):
    print(f"{name} is passed.")
else:
    print(f"{name} is not passed.")
