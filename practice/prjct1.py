name1 = input("Enter the name of the player 1: ")
name2 = input("Enter the name of the player 2: ")

print("\nChoices: ")
print("press 1, if you want to play")
print("press 2, if you do not want to play")

while True:
    ch = int(input("Enter your choice: "))

    match ch:
        case 1:
            ch1 = input("Enter your choice: ")
            ch2 = input("Enter your choice: ")

            if (ch1 == "snake" and ch2 == "water"):
                print(f"{name1} is the winner!")
            elif (ch1 == "snake" and ch2 == "water"):
                print(f"{name2} is the winner!")
            elif(ch1 == "water" and ch2 == "gun"):
                print(f"{name1} is the winner!")
            elif(ch2 == "water" and ch1 == "gun"):
                print(f"{name2} is the winner!")
            elif(ch1 == "gun" and ch2 == "snake"):
                print(f"{name1} is the winner!")
            elif(ch2 == "gun" and ch1 == "snake"):
                print(f"{name2} is the winner!")
            else:
                print("Match is draw!")
        case 2:
            break
        case _:
            print("Invalid input")
            
