"""
## 3. Common Elements in Two Lists  *(Medium)*

=================================================
COMMON ELEMENTS OF TWO LISTS
=================================================

Problem Statement:
Write a Python program that takes TWO lists of
integers as input and prints a new list that
contains only the elements present in BOTH
lists. Each common element must appear only
ONCE in the result, even if it occurs multiple
times in the inputs.

-------------------------------------------------
Instructions:
1. Take two lists of integers as input.
2. Use nested for loops to compare elements
   of the two lists.
3. Do NOT use:
   - set()
   - dictionaries
   - the 'in' operator on the inputs
     (you must compare element by element)
4. Build the result in a new list.
5. Make sure each common value appears at most
   ONCE in the result.
6. Print:
   - the resulting list

-------------------------------------------------
Input Example 1:
List 1: [1, 2, 3, 4, 5]
List 2: [3, 4, 5, 6, 7]

Output Example 1:
Common Elements: [3, 4, 5]

-------------------------------------------------
Input Example 2:
List 1: [1, 2, 2, 3]
List 2: [2, 2, 4]

Output Example 2:
Common Elements: [2]

-------------------------------------------------
Explanation:
For lists [1,2,3,4,5] and [3,4,5,6,7]:
   3, 4, 5 are present in both -> [3, 4, 5]

For lists [1,2,2,3] and [2,2,4]:
   2 is the only common value. Even though it
   appears twice in both lists, the result
   contains it only once -> [2].
=================================================

"""
n1 = int(input("Enter the number of inputs for first list: "))
d3 = []
d1 = []
for i in range(n1):
    d1.append(int(input("Enter: ")))
n2 = int(input("Enter the number of inputs for second list: "))
d2 = []
for i in range(n2):
    d2.append(int(input("Enter: ")))
for i in d1:
    for j in d2:
        if i == j:
            d3.append(i)
i = 0
while i < len(d3):
    j = i + 1
    while j < len(d3):
        if d3[i] == d3[j]:
            d3.pop(j)
        else:
            j += 1
    i += 1
print(d3)