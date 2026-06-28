#input
n = int(input("Enter the number of inputs: "))
d = []
for i in range(n):
    d.append(int(input("Enter: ")))

l1 = [i * i for i in d]
print(l1)

#comperehension using only if condition
l2 = [i for i in d if i % 2 == 0]
print(l2)
'''if only if is used, write the if statement after the for loop'''

#comperehension using both if and else
l3 = [True if i % 2 == 0 else False for i in d]
print(l3)
'''if both if and else is used, then write the condition before the for loop'''
