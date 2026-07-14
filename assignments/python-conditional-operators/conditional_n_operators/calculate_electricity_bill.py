"""
=================================================
ELECTRICITY BILL CALCULATOR
=================================================

Problem Statement:
Write a Python program to calculate electricity bill.

-------------------------------------------------
Conditions:
1. First 100 units  -> ₹5 per unit
2. Next 100 units   -> ₹7 per unit
3. Above 200 units  -> ₹10 per unit


-------------------------------------------------
Input Example:
250

Output Example:
Total Bill = ₹1700

-------------------------------------------------
Hints:
Break the problem into multiple conditions.

=================================================
"""

# Write your code below this line
name=input("Enter your name: ")
unit=int(input("Enter the units used: "))
if(unit<=100):
    ttl_prc=unit*5
elif((unit>100)and(unit<=200)):
    ttl_prc=(100*5)+((unit-100)*7)
else:
    ttl_prc=(100*5)+(100*7)+((unit-200)*10)
print("\n")
print("BILL")
print(f"Name:- {name}")
print(f"Units used:- {unit}")
print(f"total price:- ₹{ttl_prc}")
print("\n")