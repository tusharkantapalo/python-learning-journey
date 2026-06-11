try:
    string = input("Enter the string: ")

    vowel_no = {}

    vowel_l = "aeiou"
    vowel_u = "AEIOU"

    for i in string:
        if i in vowel_l or i in vowel_u:
            if i in vowel_no:
                vowel_no[i] += 1
            else:
                vowel_no[i] = 1

    print(vowel_no)
except Exception:
    print("Something wrong happend!")

finally:
    print("__________CODE EXECUTION COMPLETED__________")