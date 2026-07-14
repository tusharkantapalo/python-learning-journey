"""
## 3. Words Containing All Five Vowels  *(Medium)*

=================================================
WORDS WITH ALL VOWELS
=================================================

Problem Statement:
Read the text file `sowpods.txt` and PRINT
every word that contains ALL FIVE vowels
('a', 'e', 'i', 'o', 'u') at least once.
The order of the vowels does NOT matter, and
the check should be case-insensitive.


-------------------------------------------------
Input Example (sowpods.txt sample):
education
sequoia
facetious
hello
audio
unequivocal

Output Example:
education
sequoia
facetious
unequivocal
Total words with all vowels: 4

-------------------------------------------------
Explanation:
- "education" contains a, e, i, o, u -> yes
- "sequoia"   contains a, e, i, o, u -> yes
- "facetious" contains a, e, i, o, u -> yes
- "hello"     missing a, i, o, u     -> no
- "audio"     missing e               -> no
- "unequivocal" contains a,e,i,o,u   -> yes
=================================================

"""


path = input("Enter thae path of the file: ")

try:
    cnt = 0
    
    with open(path, "r") as fp:
        for words in fp:
            word = words.strip().lower()
            if 'a' in word and 'e' in word and 'i' in word and 'o' in word and 'u' in word:
                print(word)
                cnt += 1

    print(f"Total words with all vowels: {cnt}")

except FileNotFoundError:
    print("File not found!")

finally:
    print("__________CODE EXECUTION COMPLETED__________")
