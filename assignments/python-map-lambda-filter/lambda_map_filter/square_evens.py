"""
## 1. Square the Even Numbers  *(Easy)*

=================================================
SQUARE EVEN NUMBERS WITH MAP & FILTER
=================================================

Problem Statement:
Write a Python program that takes a list of
integers and returns a NEW list containing
the SQUARES of only the EVEN numbers from the
original list.

You MUST solve this using:
   - filter() with a lambda
   - map()    with a lambda


-------------------------------------------------
Input Example 1:
[1, 2, 3, 4, 5, 6]

Output Example 1:
Squared Evens: [4, 16, 36]

-------------------------------------------------
Input Example 2:
[7, 9, 11]

Output Example 2:
Squared Evens: []

-------------------------------------------------
Explanation:
For [1, 2, 3, 4, 5, 6]:
   filter (even)  -> [2, 4, 6]
   map    (n*n)   -> [4, 16, 36]
=================================================

"""
n = int(input("Enter the nimber of inputs: "))
list_of_numbers = []
for i in range(n):
    list_of_numbers.append(int(input("Enter: ")))
list_of_even_numbers = list(filter(lambda x: x % 2 == 0, list_of_numbers))
list_of_squares_numbers = list(map(lambda x: x ** 2, list_of_even_numbers))
print(list_of_squares_numbers)