"""
## 1. Count Vowels in a String

=================================================
VOWEL COUNTER
=================================================

Problem Statement:
Write a Python program that takes a string as
input and counts how many vowels (a, e, i, o, u)
it contains. The check must be case-insensitive.

-------------------------------------------------
Instructions:
1. Take a string as input.
2. Use a for loop to traverse each character.
3. Treat uppercase and lowercase vowels as same.
4. Print:
   - total vowel count

Note: use ASCII  check for letters, and compare. 'e', 'i', 'o', '

-------------------------------------------------
Input Example:
Hello World

Output Example:
Vowel Count: 3

-------------------------------------------------
Explanation:
H e l l o   W o r l d
  ^       ^       ^
'e', 'o', 'o' are vowels -> 3 vowels.
=================================================

"""
exp = input("Enter the expression: ")
vwl_l = 'aeiou'
vwl_u = 'AEIOU'
cnt_vwl = 0
for i in range(0,len(exp),1):
    if((exp[i] in vwl_l) or (exp[i] in vwl_u)):
        cnt_vwl += 1
print(f"Number of vowels is {cnt_vwl}")