"""
This is the bigdigits program
It does what is described in the assignment for it
"""

import sys


def return_digits(number:str) -> [str]:
    """
    Create a list of strings.
    When concatenated with newlines, makes a list of
    numbers made of these numbers
    Args:
        number: the number to be transformed
    Returns:
        [str]: list of 7 lines
    >>> return_digits('12')
    ' 1  222 \\n11 2   2\\n 1 2  2 \\n 1   2  \\n 1  2   \\n 1 2    \\n11122222'
    """
    return "\n".join(
            "".join(
                Digits[int(num)][i].replace("*", num)
                for num in number
                ) for i in range(7)
            )


Zero = ["  ***  ",
        " *   * ",
        "*     *",
        "*     *",
        "*     *",
        " *   * ",
        "  ***  "]
One = [" * ", "** ", " * ", " * ", " * ", " * ", "***"]
Two = [" *** ", "*   *", "*  * ", "  *  ", " *   ", "*    ", "*****"]
Three = [" *** ", "*   *", "    *", "  ** ", "    *", "*   *", " *** "]
Four = ["   *  ", "  **  ", " * *  ", "*  *  ", "******", "   *  ", "   *  "]
Five = ["*****", "*    ", "*    ", " *** ", "    *", "*   *", " *** "]
Six = [" *** ", "*    ", "*    ", "**** ", "*   *", "*   *", " *** "]
Seven = ["*****", "    *", "   * ", "  *  ", " *   ", "*    ", "*    "]
Eight = [" *** ", "*   *", "*   *", " *** ", "*   *", "*   *", " *** "]
Nine = [" ****", "*   *", "*   *", " ****", "    *", "    *", "    *"]
Digits = [Zero, One, Two, Three, Four, Five, Six, Seven, Eight, Nine]

try:
    digits = sys.argv[1]
    print(return_digits(digits))

except IndexError:
    print("usage: bigdigits.py <number>")
except ValueError as err:
    print(err, "in", digits)

