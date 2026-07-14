"""
## 5. First Non-Repeating Character

=================================================
FIRST NON-REPEATING CHARACTER
=================================================

Problem Statement:
Write a Python program that takes a string as
input and finds the FIRST character that does
not repeat anywhere else in the string.
If every character repeats, print a suitable
message.

-------------------------------------------------
Instructions:
1. Take a string as input.
2. Use a for loop to go through each character
   of the string from left to right.
3. For each character, use ANOTHER for loop
   (nested loop) to count how many times that
   character appears in the entire string.
4. The FIRST character whose count is exactly 1
   is the answer.
5. Do NOT use:
   - lists
   - dictionaries
   - sets
   - str.count()
   - collections module
6. Print:
   - the first non-repeating character
   - or a message if none exists

-------------------------------------------------
Input Example 1:
swiss

Output Example 1:
First Non-Repeating Character: w

-------------------------------------------------
Input Example 2:
aabbcc

Output Example 2:
No non-repeating character found

-------------------------------------------------
Explanation:
For "swiss":
   s -> appears 3 times
   w -> appears 1 time   <-- first unique
   i -> appears 1 time
   s -> ...
   s -> ...
The first character with a count of 1 is 'w'.

For "aabbcc":
Every character repeats, so there is no
non-repeating character.
=================================================

"""
exp = input("Enter the expression: ")
for i in range(0, len(exp) - 1, 1):
    cnt = 0
    for j in range(len(exp)):
        if(exp[i] == exp[j]):
            cnt += 1
    if cnt == 1:
        char = exp[i]
        flag = True
        print(f"First non repeated character is {char}")
        break
if flag == False:
    print("No non repeated character present.")