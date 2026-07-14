"""
=================================================
CHARACTER FREQUENCY COUNTER
=================================================

Problem Statement:
Write a Python program to count how many times
a character appears in a string.

-------------------------------------------------
Instructions:
1. Take input from the user:
   - a string
   - a character
2. Use loop and conditional statements.
3. Print character count.

-------------------------------------------------
Input Example:
String: programming
Character: g

Output Example:
2
-------------------------------------------------
Expected Concepts:
- loops
- strings
- operators
- logical thinking

=================================================
"""

# Write your code below this line
exp=input("Enter the character: ")
char=input("Enter the character: ")
cnt=0
for i in range(0,len(exp),1):
    if(char==exp[i]):
        cnt+=1
print(f"{char} is repeated {cnt} times.")