exp = input("Enter the string: ")

d = {} #not d=[], this is list, but we want dictionary

# Counting frequency of each character
for ch in exp:
    if ch in d:
        d[ch] += 1
    else:
        d[ch] = 1

# Finding first non-repeated character
for ch in exp:
    if d[ch] == 1:
        print(f"First non-repeated character is: {ch}")
        break