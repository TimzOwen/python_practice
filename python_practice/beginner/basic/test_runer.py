# write a function that returns a sentence with its characters in reverse oder

from curses import init_pair
from ntpath import join


def reverse_sentence():
    words = input("Enter words to reverse: ")
    split_word = words.split()
    join_word = " ".join(split_word[::-1])
    return join_word

print(reverse_sentence())