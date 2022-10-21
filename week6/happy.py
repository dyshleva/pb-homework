"""
Happy numbers submission
"""

from math import log, ceil


def happy_number(number: int) -> bool:
    """
    Check is a number is happy

    Args:
        number: the number
    Returns:
        bool: whether a number is hppy
    >>> happy_number(12345)
    False
    >>> happy_number(43211234)
    True
    >>> happy_number(191234)
    True
    """
    if number < 100:
        return number % 10 == number // 10

    strlen = 2 ** ceil(log(len(str(number)), 2))

    stringified = str(number).rjust(strlen, "0")

    head = sum(map(int, stringified[: int(strlen / 2)]))
    tail = sum(map(int, stringified[int(strlen / 2) :]))

    return head == tail and happy_number(int(str(head) + str(tail)))


def count_happy_numbers(bound: int) -> int:
    """
    Count happy numbers for first n naturals
    Args:
        n: upper bound
    Returns:
        int: the number of happy numbers in first n naturals
    >>> count_happy_numbers(120)
    11
    """

    return sum(int(happy_number(x)) for x in range(1, bound + 1))


def happy_numbers(low: int, high: int) -> list:
    """
    Generates a list of a range

    Args:
        m: lower bound
        n: higher bound
    Returns:
        list: list of a range
    >>> happy_numbers(120, 121)
    [120, 121]
    """
    return list(range(low, high + 1))
