"""
Lab 4 task 1 submission
"""

# [1, 5, 6, 7, 12, 14, 17, 18, 22, 23, 24, 27]
def get_number():
    """
    Get number
    Yes, the doc for this is needed too
    """
    number = 72
    return number


# Complete all of the following functions. Currently they all just
# 'pass' rather than explicitly return value, which means that they
# implicitly return None. They all include doctests, which you can
# test by running this file.

# The doctests are just examples. Feel free to add your own doctests.

# ****************************************
# Problem 1
# ****************************************
def get_position(ch: str) -> int:
    """
    Return positon of letter in ascii order.
    If argument is not a letter function should return None.

    :param ch: char to be checked

    :rtype: int: the position of char in  the alphabet

    >>> get_position('A')
    1
    >>> get_position('z')
    26
    >>> get_position('Dj')

    """
    if not isinstance(ch, str):
        return None
    if len(ch) == 1:
        return ord(ch.upper()) - 64
    return None


# ****************************************
# Problem 5
# ****************************************
def type_by_sides(a: float, b: float, c: float) -> str:
    """
    Detect the type of triangle by it's sides and return type as string
    ("right angled triangle", "obutuse triangle", "acute triangle"). If there is no
    triangle with such sides, then function should return None.

    :param a: first side
    :param b: second side
    :param a: third side

    :rtype: str: one of three strings described above

    >>> type_by_sides(3, 3, 3)
    'acute triangle'
    >>> type_by_sides(3, 4, 5)
    'right angled triangle'
    >>> type_by_sides(3, 3, 2015)
    """
    max_side = max(a, b, c)
    sides = [a, b, c]
    sides.remove(max_side)

    if a <= 0 or b <= 0 or c <= 0 or sum(sides) < max_side:
        return None

    if sum(map(lambda x: x**2, sides)) < max_side**2:
        return "obtuse triangle"
    if sum(map(lambda x: x**2, sides)) == max_side**2:
        return "right angled triangle"
    if sum(map(lambda x: x**2, sides)) > max_side**2:
        return "acute triangle"
    return None


# ****************************************
# Problem 6
# ****************************************
def remove_spaces(s: str) -> str:
    """
    Remove all additional spaces in string and return a new string without additional spaces.
    If argument is not a string function should return None.

    :param s: string to be trimmed

    :rtype: str: processde string

    >>> remove_spaces("I'll make     him an     offer he can't refuse.")
    "I'll make him an offer he can't refuse."
    >>> remove_spaces("Great    men     are    not born great, they grow great...")
    'Great men are not born great, they grow great...'
    >>> remove_spaces(2015)

    """
    if not isinstance(s, str):
        return None

    return ' '.join(s.split())


# ****************************************
# Problem 7
# ****************************************
def print_column(s: str) -> None:
    """
    Print the string. This is an additional function for convert_to_column

    :param s: string to be printed
    """
    result = convert_to_column(s)
    if result is not None:
        print(result)


def convert_to_column(s):
    """
    Convert string to a column of words.
    If argument is not a string function should return None.
    The function removes all non-letter characters

    :param s: string to be processed

    :rtype: str: processed string

    >>> print_column("Revenge is a dish that tastes best when served cold.")
    revenge
    is
    a
    dish
    that
    tastes
    best
    when
    served
    cold
    >>> print_column("Never hate your enemies. It affects your judgment.")
    never
    hate
    your
    enemies
    it
    affects
    your
    judgment
    >>> print_column(2015)
    """
    if not isinstance(s, str):
        return None

    s = "".join(
        filter(lambda x: 65 <= ord(x) <= 90 or 97 <= ord(x) <= 122 or x == " ", s)
    )

    return "\n".join([word.lower() for word in s.split()])


# ****************************************
# Problem 12
# ****************************************
def exclude_letters(s1: str, s2: str) -> str:
    """
    Delete all letter from string s2 in string s1. If arguments aren't strings function should
    return None.

    :param s1: string to be edited
    :param s2: string with characters to be excluded

    :rtype: str: parsed string

    >>> exclude_letters("aaabb", "b")
    'aaa'
    >>> exclude_letters("abcc", "cczzyy")
    'ab'
    >>> exclude_letters(2015, "sasd")

    """
    if not isinstance(s1, str) or not isinstance(s2, str):
        return None

    return "".join(filter(lambda x: x not in s2 or not x.isalpha(), s1))


# ****************************************
# Problem 14
# ****************************************
def get_letters(n: int) -> str:
    """
    Create and return string of first n letters of an alphabet. If arguments isn't
    positive integer number function should return None.

    :param n

    >>> get_letters(0)

    >>> get_letters(1)
    'a'
    >>> get_letters(-2015)

    """
    if not isinstance(n, int) or n < 1:
        return None

    letters = [chr(x) for x in range(97, 123)]

    return ''.join(letters[0:n])


# ****************************************
# Problem 17
# ****************************************
def number_of_occurence(lst: list, s: str) -> int:
    """
    Find and return number of occurence of string s in all elements of the
    list lst. If lst isn't list of strings or s isn't string function should
    return None.

    :param lst: list of words
    :parsm s: string to occur

    :rtype: int: amount of occurences

    >>> number_of_occurence(["man", "girl", "women", "boy"], "m")
    2
    >>> number_of_occurence(["ab", "aba", "a", "b", "ba"], "ba")
    2
    >>> number_of_occurence([1, 2, 2015, 1, 3], "1")

    """
    if not isinstance(lst, list):
        return None
    for _ in lst:
        if not isinstance(_, str):
            return None

    out = map(lambda x: x.count(s), lst)

    return sum(out)


# ****************************************
# Problem 18
# ****************************************
def number_of_capital_letters(s: str) -> int:
    """
    Find and return number of capital letters in string. If argument isn't string
    function should return None.

    :param s: string to be processed

    :rtype: int: number of uppercase letters in string

    >>> number_of_capital_letters("ArithmeticError")
    2
    >>> number_of_capital_letters("EOFError")
    4
    >>> number_of_capital_letters(1)

    """
    if not isinstance(s, str):
        return None

    return sum(map(lambda x: 65 <= ord(x) <= 90, s))


# ****************************************
# Problem 22
# ****************************************
def pattern_number(sequence: list) -> tuple:
    """
    Return the longest repeating pattern
    and a number of occurences of said pattern.

    :param sequence: list of literals

    :rtype: tuple: pair of occurence and number or occurences
    >>> pattern_number([])

    >>> pattern_number([42])

    >>> pattern_number([1,2])

    >>> pattern_number([1,1])
    ([1], 2)
    >>> pattern_number([1,2,1])

    >>> pattern_number([1,2,3,1,2,3])
    ([1, 2, 3], 2)
    >>> pattern_number([1,2,3,1,2])

    >>> pattern_number([1,2,3,1,2,3,1])

    >>> pattern_number(list(range(10))*20)
    ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9,\
 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8,\
 9, 0, 1,\
 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3,\
 4, 5, 6, 7, 8, 9], 2)
    >>> pattern_number('мама')
    ('ма', 2)
    >>> pattern_number('барабан')

    """

    if len(sequence) <= 1:
        return None

    final = None
    result = [None, 0]
    for i in range(1, len(sequence) // 2 + 1):
        res = sequence[0:i]
        if (
            res is not None
            and res * int(len(sequence) / len(res)) == sequence
        ):
            result = [res, len(sequence) // i]

    if result[0] is not None:
        final = (result[0], result[1])

    return final


# ****************************************
# Problem 23
# ****************************************
def one_swap_sorting(sequence: list) -> bool:
    """
    Check if swapping two elements in the list can make it sorted

    :param sequence: list to be checked

    :rtype: bool
    >>> one_swap_sorting([0,1,2,3])
    False
    >>> one_swap_sorting([])
    False
    >>> one_swap_sorting([42])
    False
    >>> one_swap_sorting([3,2])
    True
    >>> one_swap_sorting([2,2])
    False
    >>> one_swap_sorting([5,2,3,4,1,6])
    True
    >>> one_swap_sorting([1,2,3,5,4])
    True
    """

    if len(sequence) <= 1 or sequence == sorted(sequence):
        return False

    for pos, i in enumerate(sequence):
        for j in range(len(sequence)):
            tmp = sequence
            tmp[pos] = tmp[j]
            tmp[j] = i
            if sorted(tmp) == tmp:
                return True
    return False


# ****************************************
# Problem 24
# ****************************************
def numbers_Ulam(n: int) -> list:
    """
    Returns the first n ulam numbers

    :param n: amount of numbers

    :rtype: list: list of n ulam numbers
    >>> numbers_Ulam(10)
    [1, 2, 3, 4, 6, 8, 11, 13, 16, 18]
    >>> numbers_Ulam(2)
    [1, 2]
    >>> numbers_Ulam(1)
    [1]
    """
    if n == 1:
        return [1]

    ulam = [1, 2]

    i = 3
    while len(ulam) < n:
        count = 0

        for j in range(len(ulam) - 1):
            for k in range(j + 1, len(ulam)):
                if ulam[j] + ulam[k] == i:
                    count += 1
                if count > 1:
                    break
            if count > 1:
                break
        if count == 1:
            ulam.append(i)

        i += 1

    return ulam


# ****************************************
# Problem 27
# ****************************************
def turn_over(n: int, lst: list) -> list:
    """
    Reverse first n items of the list and return it. If n <= 0, return
    the empty list. Do not consume MORE than n items of iterable.

    :param n: first n elements to be reversed
    :param lst: list to be modified

    :rtype: list: modified list

    >>> turn_over(4, ['f', 'o', 'o', 't', 'b', 'a', 'l', 'l'])
    ['t', 'o', 'o', 'f', 'b', 'a', 'l', 'l']
    >>> turn_over(5, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    [5, 4, 3, 2, 1, 6, 7, 8, 9, 10]
    >>> turn_over(10, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    >>> turn_over(-5, [])
    []

    """
    if not 0 <= n <= len(lst):
        return []
    return list(reversed(lst[0:n])) + lst[n:]


if __name__ == "__main__":
    import doctest

    print(doctest.testmod())
