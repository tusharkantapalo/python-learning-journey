"""
## 7. Find a Character in a 2D Matrix  *(Easy)*

=================================================
SEARCH CHARACTER IN A 2D MATRIX
=================================================

Problem Statement:
A 2D matrix of characters is generated using
the following code:

   table = [list("abcd"), list("efgh"), list("ijkl")]

This produces:

   a b c d
   e f g h
   i j k l

Write a Python program that takes a single
TARGET CHARACTER as input and prints the
ROW INDEX and COLUMN INDEX (0-based) of the
character in the matrix.

If the character is NOT present, print
"Not found".

-------------------------------------------------
Input Example 1:
Enter target character: h

Output Example 1:
1 3

-------------------------------------------------
Input Example 2:
Enter target character: z

Output Example 2:
Not found

-------------------------------------------------
Explanation:
table = [
   ['a', 'b', 'c', 'd'],   # row 0
   ['e', 'f', 'g', 'h'],   # row 1
   ['i', 'j', 'k', 'l'],   # row 2
]
'h' is in row 1, column 3 -> print "1 3".
'z' does not exist in the matrix -> print
"Not found".
=================================================

"""
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
table = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(input(f"Enter character at ({i},{j}): "))
    table.append(row)
target = input("Enter target character: ")
found = False
for i in range(len(table)):
    for j in range(len(table[i])):
        if table[i][j] == target:
            print(i, j)
            found = True
            break
    if found:
        break
if not found:
    print("Not found")