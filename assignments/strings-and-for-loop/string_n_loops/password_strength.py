"""
=================================================
PASSWORD STRENGTH CHECKER
=================================================

Problem Statement:
Write a Python program to check password strength.

-------------------------------------------------
Conditions:
A password is strong if:
1. Length is at least 8
2. Contains at least one digit
3. Contains at least one uppercase letter

-------------------------------------------------
Instructions:
1. Take password input from user.
2. Use loops and conditional statements.
3. Print:
   - "Strong Password"
   - "Weak Password"

-------------------------------------------------
Input Example:
Python123

Output Example:
Strong Password

-------------------------------------------------
Hints:
Use:
isdigit()
isupper()

-------------------------------------------------
Expected Concepts:
- loops
- string functions
- operators
- conditional statements

=================================================
"""

# Write your code below this line
pas=input("Enter the password: ")
cnt_dgt=0
cnt_upcs=0
for i in range(0,len(pas),1):
    if pas[i].isdigit():
        cnt_dgt+=1
    if pas[i].isupper(): #((pas[i]>='A')and(pas[i]<='Z')):
        cnt_upcs+=1
if((len(pas)>=8)and(cnt_dgt>=1)and(cnt_upcs>=1)):
    print("Strong Password")
else:
    print("Weak Password")