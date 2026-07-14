"""
=================================================
PALINDROME CHECKER
=================================================

Problem Statement:
Write a Python program to check whether a string
is palindrome or not.

-------------------------------------------------
Instructions:
1. Take string input.
2. Reverse the string.
3. Compare original and reversed string.
4. Print:
   - "Palindrome"
   - "Not Palindrome"

-------------------------------------------------
Input Example:
madam

Output Example:
Palindrome

-------------------------------------------------
Hints:
Use slicing or loop.

-------------------------------------------------
Expected Concepts:
- operators
- string slicing
- conditional statements

=================================================
"""

# Write your code below this line
exp=input("Enter the expression: ")
if(exp[ : :1]==exp[ : : -1]):
    print(f"{exp} is palindrome.")
else:
    print(f"{exp} is not palindrome.")