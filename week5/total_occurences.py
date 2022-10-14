"""
total_occurences asssignment
"""


def total_occurrences(s1, s2, ch):
    """
    (str, str, str) -> int
    Precondition: len(ch) == 1
    Return the total number of times that ch occurs in s1 and s2.
    Args:
        s1: first string
        s2: second string
        ch: char

    Returns:
        int: the number of occurences
    >>> total_occurrences('color', 'yellow', 'l')
    3
    >>> total_occurrences('red', 'blue', 'l')
    1
    >>> total_occurrences('green', 'purple', 'b')
    0
    """
    if len(ch) != 1:
        raise ValueError

    concatenated = s1 + s2
    return concatenated.count(ch)
