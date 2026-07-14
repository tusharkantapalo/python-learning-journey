exp = input("Enter a string: ")
for i in range(0,len(exp),1):
    if(((exp[i]>='a')and(exp[i]<='z'))or((exp[i]>='A')and(exp[i]<='Z'))):
        continue #print("True")
    else:
        print("False")
        break
else:  #else is also used with for loop
    print("True")