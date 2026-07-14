"""
=================================================
CONSECUTIVE CHARACTER COUNTER
=================================================

Problem Statement:
Write a Python program to count the maximum number
of consecutive occurrences of the same character
in a string.

-------------------------------------------------
Instructions:
1. Take a string as input.
2. Use a for loop.
3. Find the longest consecutive repeating character.
4. Print:
   - character
   - count

-------------------------------------------------
Input Example:
aaabbccccdde

Output Example:
Character: c
Count: 4

-------------------------------------------------
Explanation:
a -> 3 times
b -> 2 times
c -> 4 times
d -> 2 times
e -> 1 time

Highest consecutive count:
c -> 4

-------------------------------------------------
Hints:
1. Compare current character with previous character.
2. Keep track of:
   - current count
   - maximum count
3. Update maximum when needed.

-------------------------------------------------
Expected Concepts:
- Don't use dictionary.
- for loops
- string indexing
- operators
- conditional statements
- logical thinking

=================================================
"""

# Write your code below this line
exp=input("Enter the expression: ")
max_cnt=0
cnt=0
for i in range(1,len(exp),1):
   if(exp[i]==exp[i-1]):
        cnt+=1
   else:
       cnt=1
   if(cnt>max_cnt):
      max_cnt=cnt
      exp1=exp[i]
print(f"{exp1} is occured maximum of {max_cnt}")