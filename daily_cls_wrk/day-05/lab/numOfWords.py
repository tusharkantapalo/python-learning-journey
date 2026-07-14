'''exp = input("Enter the sentence: ")
cnt = 1
for i in range(len(exp)):
    if(exp[i] == ' '):
        cnt += 1
print(f"Number of words is: {cnt}")'''
#Here it is not universal
#using split
exp = input("Enter the sentence: ")
d = exp.split()
print(f"Number of words is {len(d)}")