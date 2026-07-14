"""
## 3. Check if a Number is Prime

=================================================
PRIME NUMBER CHECK
=================================================

Problem Statement:
Write a Python program that takes a positive
integer as input and checks whether it is a
PRIME number.

A prime number is a natural number greater
than 1 that is divisible only by 1 and itself.

-------------------------------------------------
Instructions:
1. Take a positive integer n as input.
2. Use a for loop with range() to test possible
   divisors of n.

-------------------------------------------------
Input Example 1:
7

Output Example 1:
Prime

-------------------------------------------------
Input Example 2:
12

Output Example 2:
Not Prime

-------------------------------------------------
Explanation:
7 is divisible only by 1 and 7, so it is Prime.
12 is divisible by 2, 3, 4, 6, so it is Not Prime.
=================================================

"""
num = int(input("Enter the number: "))
for i in range(2, num):
    if (num % i == 0):
        print(f"{num} is not a prime number")
        break
    else:
        continue
else:
    print(f"{num} is a prime number.")