# %load exercises/generators.py
"""Generator Exercises."""
import string

def is_prime(number):
    """Return True if candidate number is prime."""
#     for n in range(2, number): 
#         if number % n ==0: 
#             return False 
#         return True
    return all(
        number % n != 0 
        for n in range(2,number)
              )

def all_together(*iterables):
    """String together all items from the given iterables."""  
    for iterable in iterables: 
        for x in iterable: 
            yield x


def interleave(ranges):
    """Return iterable of one item at a time from each list."""


def translate():
    """Return a transliterated version of the given sentence."""


def parse_ranges(ranges):
    """Return a list of numbers corresponding to number ranges in a string"""
    hasil = []
    if ',' in ranges: 
        temp = ranges.split(',')
        for i in temp:
            parse_ranges(i)
    else: 
        [hasil.append(int(x)) for x in ranges.split('-')]
        return iter(range(hasil[0], hasil[1]+1))

def first_prime_over():
    """Return the first prime number over a given number."""


def is_anagram(word1,word2):
    """Return True if the given words are anagrams."""
    return sorted([
        x 
        for x in word2.lower() 
        if x in string.ascii_lowercase
    ])==sorted([
        x 
            for x in word1.lower() 
            if x in string.ascii_lowercase
    ])
    
