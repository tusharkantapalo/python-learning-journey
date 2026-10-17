'''
Write a python function to print first n lines of the following pattern:
***
** - for n = 3
*
'''

def res(n):

    for i in range(n , 0, -1):
        for j in range(0, i):
            print("*",end=" ")
        print("\n")

n = int(input("Enter the number: "))

res(n)
