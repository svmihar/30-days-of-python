# %load exercises/lists.py
"""List comprehension exercises"""


def get_vowel_names(names):
    """Return a list containing all names given that start with a vowel."""
    return [a for a in names if a[0].upper() in 'AIUEO']


def power_list(fav):
    """Return a list that contains each number raised to the i-th power."""
    return [
        num**i 
            for i, num in enumerate(fav)
    ]

  
def flatten(matrix):
    """Return a flattened version of the given 2-D matrix (list-of-lists)."""
    return [item 
            for row in matrix 
                for item in row  # this in only an alignment
           ]

def reverse_difference(matrix):
    """Return list subtracted from the reverse of itself."""
    return [
        [-n for n in row]
        for row in matrix
    ]
    

def matrix_add():
    """Add corresponding numbers in given 2-D matrices."""
    pass


def transpose():
    """Return a transposed version of given list of lists."""
    pass


def get_factors():
    """Return a list of all factors of the given number."""
    pass


def triples():
    """Return list of Pythagorean triples less than input num."""
    pass

