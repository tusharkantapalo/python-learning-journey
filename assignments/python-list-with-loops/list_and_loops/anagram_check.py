"""
## 5. Check if Two Strings are Anagrams (*Hard*)

=================================================
ANAGRAM CHECK
=================================================

Problem Statement:
Write a Python program that takes TWO strings
as input and checks whether they are ANAGRAMS
of each other.

Two strings are anagrams if they contain the
exact same characters with the same frequency,
just in a different order. The check must be
case-insensitive and should ignore spaces.

-------------------------------------------------
Instructions:
1. Take two strings as input.
2. Convert both strings to lowercase and
   remove all spaces using a for loop
   (do NOT use str.replace()).
3. If their lengths are different, they cannot
   be anagrams.
4. Do NOT use:
   - sorted() or .sort()
   - dictionaries
   - sets
   - collections.Counter
   - str.count()
5. Print:
   - "Anagram" or "Not Anagram"

-------------------------------------------------
Input Example 1:
String 1: Listen
String 2: Silent

Output Example 1:
Anagram

-------------------------------------------------
Input Example 2:
String 1: Hello
String 2: World

Output Example 2:
Not Anagram

-------------------------------------------------
Explanation:
"Listen" -> "listen"
"Silent" -> "silent"
Both have the same characters with the same
frequency (l, i, s, t, e, n) -> Anagram.

"Hello" and "World" do not contain the same
characters, so they are Not Anagram.
=================================================

"""
exp1 = input("Enter the first string: ")
exp2 = input("Enter the seond string: ")
i = 0
j = 0
if len(exp1) == len(exp2):
    while i < len(exp1):
        j = 0
        while j < len(exp2):
            if exp1[i] == exp2[j]:
                j += 1
            else:
                break
        i += 1
    print("Anagram")
else:
    print("Not Anagram")