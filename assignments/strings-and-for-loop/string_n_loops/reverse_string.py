"""
=================================================
REVERSE A STRING
=================================================

Problem Statement:
Write a Python program to reverse a string.

-------------------------------------------------
Instructions:
1. Take string input from the user.
2. Reverse the string using:
   - slicing AND
   - loop
3. Print reversed string.

-------------------------------------------------
Input Example:
Python

Output Example:
nohtyP

-------------------------------------------------
Expected Concepts:
- string slicing
- loops
- indexing

=================================================
"""

# Write your code below this line
j=0
exp1=''
exp=input("Enter the expression: ")
print("Reversing using slicing: ")
print(exp[ : :-1])
for i in range(len(exp)-1, -1,-1):
    exp1+=exp[i]
print("Reversing using loop: ")
print(exp1)