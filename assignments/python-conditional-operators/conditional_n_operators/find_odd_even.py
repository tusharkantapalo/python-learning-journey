"""
=================================================
EVEN OR ODD CHECKER
=================================================

Problem Statement:
Write a Python program to check whether a number
is Even or Odd.

-------------------------------------------------
Input Example:
7

Output Example:
Odd

=================================================
"""

# Write your code below this line
num=int(input("Enter the number: "))
if(num==1):
    print(f"1 is special number")
elif((num%2)==0):
    print(f"{num} is even")
else:
    print(f"{num} is odd")