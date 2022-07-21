# write a function that returns a sentence with its characters in reverse oder
# used 5 diffrrenr options to solve this question 

from curses import init_pair
from ntpath import join


def reverse_sentence(words): # using string and split 
    split_word = words.split()
    join_word = " ".join(split_word[::-1])
    return join_word
print(reverse_sentence("This is reversed"))

def word_join(x):   #using one lineer killer 
    return " ".join(x.split()[::-1])

print(word_join("This is owen testing"))

def word_reversedby(y): # using reversed keyword
    w = y.split()
    return " ".join(reversed(w))
print(word_reversedby("using reversed key word"))

def word_split_join(w):
    w_split = w.split()
    w_split.reverse()
    return " ".join(w_split)
print(word_split_join("This is reversed too"))

