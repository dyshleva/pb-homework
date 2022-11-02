"""
numbersequence.py assignment submission
"""
from typing import List


def check_for_even_bits(number: int) -> bool:
    """
    Check for the condition in the assignment
    Args:
        number: number to be checked
    Returns:
        bool: whether a number has an even amount of one in its binary representation,
            excluding the least one
    >>> check_for_even_bits(1)
    False
    >>> check_for_even_bits(2)
    False
    >>> check_for_even_bits(3)
    False
    >>> check_for_even_bits(6)
    True
    """
    bit_sum = sum(map(int, bin(number)[2:-1]))
    return bit_sum != 0 and bit_sum % 2 == 0


def pyramidal_numbers(length: int) -> List[int]:
    """
    The assignment function

    Args:
        length: the length of the output array

    Returns:
        List[int]: an array of proper pyramidal numbers
    >>> pyramidal_numbers(3)
    [12, 792, 1125]
    >>> pyramidal_numbers(4)
    [12, 792, 1125, 2046]
    """
    output = []

    iterator = 0
    while len(output) < length:
        ith_pyramid = iterator * (iterator + 1) * (3 * iterator - 2) // 2
        if check_for_even_bits(ith_pyramid):
            output.append(ith_pyramid)
        iterator += 1

    return output
