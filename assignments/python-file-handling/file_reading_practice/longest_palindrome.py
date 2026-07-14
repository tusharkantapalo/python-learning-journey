"""
## 5. Longest Palindrome in the File  *(Hard)*

=================================================
LONGEST PALINDROME
=================================================

Problem Statement:
Read the text file `sowpods.txt` and find the
LONGEST PALINDROME word in the file.

If multiple palindromes share the maximum
length, print ALL of them.

-------------------------------------------------
Input Example (sowpods.txt sample):
level
radar
noon
civic
deified
racecar
rotator
malayalam

Output Example:
Longest palindrome length: 9
malayalam

-------------------------------------------------
Explanation:
Lengths of the palindromes in the sample:
   level    -> 5
   radar    -> 5
   noon     -> 4
   civic    -> 5
   deified  -> 7
   racecar  -> 7
   rotator  -> 7
   malayalam -> 9
The longest is "malayalam" with 9 characters.
=================================================

"""


def is_palindrome(word):
    
   word = word.strip().lower()

   if word == word[ : :-1]:
      return True
   else:
      return False


path = input("Enter thae path of the file: ")

try:
   palindrome = []

   with open(path, "r") as fp:
      for word in fp:
         if is_palindrome(word):
            palindrome.append(word.strip())

   longest = palindrome[0]
   long_list = set()

   for word in palindrome:
      if len(word) > len(longest):
         longest = word

   long_list.add(longest)

   for word in palindrome:
      if len(word) == len(longest):
         long_list.add(word)

   print(f"The longest palindromes are/is: {long_list}")

except FileNotFoundError:
    print("File not found!")

finally:
    print("__________CODE EXECUTION COMPLETED__________")
