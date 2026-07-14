"""
## 6. Words in sonnet_words.txt but NOT in sowpods.txt  *(Hard)*

=================================================
WORDS UNIQUE TO THE SONNET
=================================================

Problem Statement:
Read the text files `sowpods.txt` and
`sonnet_words.txt`. PRINT every word that
appears in `sonnet_words.txt` but does NOT
appear in `sowpods.txt`.

This problem is about CHOOSING THE RIGHT DATA
STRUCTURE. If you check each sonnet word
against the SOWPODS list with a nested loop,
the work is O(N*M). Using SETS turns the
membership check into O(1), giving you an
overall O(N + M) algorithm.

-------------------------------------------------
Input Example:
sowpods.txt sample:
   thee
   love
   summer
   day
   eyes
   shall
   more

sonnet_words.txt sample:
   shall
   i
   compare
   thee
   to
   a
   summer
   day

Output Example:
Words in sonnet but not in sowpods:
['a', 'compare', 'i', 'to']
Total: 4

-------------------------------------------------
Explanation:
sonnet words -> {'shall', 'i', 'compare',
                 'thee', 'to', 'a', 'summer',
                 'day'}
sowpods set   -> {'thee', 'love', 'summer',
                  'day', 'eyes', 'shall',
                  'more'}
Difference (sonnet - sowpods)
              -> {'i', 'compare', 'to', 'a'}
After sorting -> ['a', 'compare', 'i', 'to'].
=================================================

"""


path1, path2 = input("enter the path of the first file: "), input("enter the path of the second file: ")

try:
   sonnet_words = set()
   sowpods_words = set()

   with open(path1, "r") as fp1:
      for words in fp1:
         sonnet_words.add(words.strip())
   
   with open(path2, "r") as fp2:
       for words in fp2:
          sowpods_words.add(words.strip())

   answer = sonnet_words - sowpods_words

   print(f"Words unique to sonnet words are: {answer} and number of words is: {len(answer)}")

except FileNotFoundError:
   print("File not found!")

finally:
    print("__________CODE EXECUTION COMPLETED__________")
    