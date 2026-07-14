"""
=================================================
LOGIN VALIDATOR SYSTEM
=================================================

Problem Statement:
Write a Python program for a simple login system.

-------------------------------------------------
Conditions:
1. Username should be: admin
2. Password should be: python123

-------------------------------------------------
Requirements:
1. If both username and password are correct:
      Print "Login Successful"

2. If username is wrong:
      Print "Invalid Username"

3. If password is wrong:
      Print "Invalid Password"

4. If both are wrong:
      Print "Invalid Credentials"

-------------------------------------------------
Input Example:
Username: admin
Password: test

Output Example:
Invalid Password

=================================================
"""
# Write your code below this line
name=input("Enter username: ")
paswrd=input("Enter password: ")
if((name=="admin")and(paswrd=="python123")):
    print("Login Successful")
elif((name=="admin")and(paswrd!="python123")):
    print("Invalid Password")
elif((name!="admin")and(paswrd=="python123")):
    print("Invalid Username")
else:
    print("Invalid Credentials")