try:
    string = input("Enter the string: ")

    org = ""

    for i in string:
        if i not in org:
            org += i

    print(org)
except Exception:
    print("There is some error!")

finally:
    print("__________CODE EXECUTION COMPLETED__________")