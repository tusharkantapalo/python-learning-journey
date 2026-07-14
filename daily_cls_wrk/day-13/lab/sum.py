def sum_of_numbers_in_string(s):

    try:
        total = 0
        for ch in s:
            if ch.isdigit():
                total += int(ch)
        return total
    except ValueError:
        return "ValueError occured!"
    


s = input("Enter the string: ")
res = sum_of_numbers_in_string(s)
print("Sum of digits:", res)