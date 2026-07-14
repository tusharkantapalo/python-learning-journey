"""
=================================================
LARGEST OF THREE NUMBERS
=================================================

Problem Statement:
Write a Python program to find the largest among three numbers.

-------------------------------------------------
Input Example:
10
45
23

Output Example:
45 is the largest number

-------------------------------------------------
Hints:
Use if-elif-else carefully.

=================================================
"""

# Write your code below this line
num1=int(input("enter the first number: "))
num2=int(input("Enter the second numbee: "))
num3=int(input("Enter the third numbee: "))
if(num1>num2):
    num=num1
elif(num1<num2):
    num=num2
if(num<num3):
    num=num3
print(f"The greatest number among these three is: {num}")