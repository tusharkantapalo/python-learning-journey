"""
## 4. Word Frequency in a Sentence  *(Medium)*

=================================================
WORD FREQUENCY ANALYZER
=================================================

Problem Statement:
Write a Python FUNCTION called `count_word_frequency`
that takes a sentence (string) as input and
returns a DICTIONARY where:
   - key   -> a unique word from the sentence
   - value -> the number of times that word
              appears

The check must be case-insensitive
("Hello" and "hello" are the same word).
The function must also return a SET of all
unique words as a second value.

So the function returns a TUPLE:
        (frequency_dict, unique_words_set)

-------------------------------------------------
Instructions:
1. Define a function:
      def count_word_frequency(sentence):
2. Convert the sentence to lowercase.
3. Split the sentence into words.
4. Use a for loop to build the frequency
   dictionary.
5. Build a set of unique words.
6. Do NOT use:
   - collections.Counter
   - dict comprehensions
   - set comprehensions
7. Return the (dict, set) tuple and print it.

-------------------------------------------------
Input Example:
"the quick brown fox jumps over the lazy dog the fox is quick"

Output Example:
Frequency: {
   'the': 3, 'quick': 2, 'brown': 1, 'fox': 2,
   'jumps': 1, 'over': 1, 'lazy': 1, 'dog': 1,
   'is': 1
}
Unique Words: {'the', 'quick', 'brown', 'fox',
   'jumps', 'over', 'lazy', 'dog', 'is'}

-------------------------------------------------
Explanation:
After lowercasing and splitting:
   the -> 3, quick -> 2, fox -> 2,
   brown, jumps, over, lazy, dog, is -> 1 each
The set holds each unique word exactly once.
=================================================

"""
def frequency_dict(exp1):
    d = {}
    t = ()
    for wrd in exp1.split():
        if wrd in d:
            d[wrd] += 1
        else:
            d[wrd] = 1
    for wrd in d:
        if d[wrd] >= 1:
            t += (wrd,)
    return d, t
exp = input("Enter the sentence: ")
exp1 = exp.lower()
exp1.split()
res, unq = frequency_dict(exp1)
print(res)
print(unq)