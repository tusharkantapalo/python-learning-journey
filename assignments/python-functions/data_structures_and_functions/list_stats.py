"""
## 3. Min, Max, and Average of a List  *(Medium)*

=================================================
LIST STATISTICS FUNCTION
=================================================

Problem Statement:
Write a Python FUNCTION called `list_stats`
that takes a list of numbers as input and
returns a TUPLE of three values:
        (minimum, maximum, average)

If the list is EMPTY, the function must
return the tuple (None, None, None).

-------------------------------------------------
Instructions:
1. Define a function:
      def list_stats(numbers):
2. Handle the empty-list case first.
3. Use a for loop to find:
   - the minimum value
   - the maximum value
   - the sum of all values
   in a SINGLE pass through the list.
4. Calculate the average from the sum and
   the length of the list.
5. Do NOT use:
   - min()
   - max()
   - sum()
   - statistics module
6. Return the three values as a tuple.
7. Call the function and print the result.

-------------------------------------------------
Input Example 1:
[5, 1, 9, 3, 7]

Output Example 1:
(1, 9, 5.0)

-------------------------------------------------
Input Example 2:
[]

Output Example 2:
(None, None, None)

-------------------------------------------------
Explanation:
For [5, 1, 9, 3, 7]:
   min     -> 1
   max     -> 9
   sum     -> 25
   average -> 25 / 5 = 5.0
The function returns (1, 9, 5.0) as a tuple.
=================================================

"""
def list_stats(d):
    sum = 0
    if len(d) == 0:
        return None, None, None
    else:
        lar = max(d)
        sma = min(d)
        for num in d:
           sum = sum + num
        avg = sum / len(d)
        return sma, lar, avg
    
n = int(input("Enter the number of inputs: "))
d = []
for i in range(n):
    d.append(int(input("Enter: ")))
low, high, avg = list_stats(d)
print(f"Smallest number is {low}\nLargest number is {high}\nAverage value is {avg}")
