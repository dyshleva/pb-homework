"""
numbersequence.py submission
"""

from typing import List


def check_for_speciality(i: int) -> bool:
    """
    Check number for narayana as shown in
    Args:
        i: int
    Returns:
        bool: whether speciality condition is met
    """
    bin_rep = list(reversed([int(x) for x in bin(i)[2:]]))
    bin_rep = bin_rep[:2] + bin_rep[3:]
    return sum(bin_rep) % 2 == 0


def narayana_sequence(i: int) -> List[int]:
    """
    Return first i special narayana sequence numbers
    Special here being that the number has an even number of
    1 bits in its binary representation, excluding the third bit

    Args:
        i - list length
    Reutnrs:
        list of special narayana numbers
    """

    lst = [1, 1, 1]
    j = 3
    while True:
        narayana = lst[j - 1] + lst[j - 3]
        lst.append(narayana)
        j += 1
        if len(list(filter(check_for_speciality, lst))) == i:
            return list(filter(check_for_speciality, lst))
