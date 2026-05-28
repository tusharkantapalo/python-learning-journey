name=input("Enter your name: ")
vowel_l='aeiou'
vowel_u='AEIOU'
cnt_n=0
cnt_v=0
cnt_c=0
cnt_s=0
for i in range( 0, len(name), 1):
    if(((name[i]>='a')and(name[i]<='z'))or((name[i]>='A')and(name[i]<='Z'))):
        if((name[i] in vowel_l)or(name[i] in vowel_u)):
            cnt_v+=1
        else:
            cnt_c+=1
    elif(name[i]==' '):
        cnt_s+=1
    else:
        cnt_n+=1
print(f"No. of vowels: {cnt_v}")
print(f"No. of consonants: {cnt_c}")
print(f"No. of non-alphabets: {cnt_n}")
print(f"No. of spaces: {cnt_s}")