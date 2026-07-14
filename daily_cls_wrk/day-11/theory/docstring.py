#function
def sum_of_two_nos(a: int, b: int) -> int:
    '''
    This function accepts two arguments and returns the sum of them
    
    arguments:
        a (int): first number
        b (int): second number
    
    returns:
        int: sum of a and b
    '''
    return a + b
'''Here (a: int) means a is of integer and also with b and 
(-> int) means the function will return int type'''


#input
a, b = int(input("Enter a: ")), int(input("Enter b: "))

sum = sum_of_two_nos(a, b)
print(sum)