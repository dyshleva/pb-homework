"""
Flavius sieve submission
"""


def sieve_flavius(flavs: int) -> list[int]:
    """
    Make a lucky numbers list

    Args:
        flavs: max lucky number

    Returns:
        list[int]: a list of luckky numbers
    >>> sieve_flavius(100)
    [1, 3, 7, 9, 13, 15, 21, 25, 31, 33, 37, 43, 49, 51, 63, 67, 69, 73, 75, 79, 87, 93, 99]
    >>> sieve_flavius(10)
    [1, 3, 7, 9]
    >>> sieve_flavius(0)
    []
    """
    if not isinstance(flavs, int) or flavs <= 0:
        return []

    base = list(range(1, flavs + 1))

    for i in range(2, flavs):
        if i in base:
            base = [x for it, x in enumerate(base) if (it + 1) % i]

    return base
