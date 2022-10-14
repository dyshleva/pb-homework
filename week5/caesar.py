"""
The caesar encoding sumbission
"""


def get_ljust(char: str) -> int:
    """
    Get the char's base value
    Example: 'a' -> 97, 'B' -> 65
    Args:
        char: char to be processed
    Returns:
        int: char's base value
    >>> get_ljust('a')
    97
    >>> get_ljust('-')
    0
    """
    match char:
        case char if 97 <= ord(char) <= 122:
            return 97
        case char if 65 <= ord(char) <= 90:
            return 65
        case _:
            return 0


def encode_letter(char: str, step: int) -> str:
    """
    Encode a single letter with caesar cipher
    Args:
        char: char to be encoded
        step: caesar's step
    Returns:
        str: encoded char
    >>> encode_letter('a', 26)
    'a'
    >>> encode_letter('i', 100)
    'e'
    """

    ljust = get_ljust(char)

    if ljust == 0:
        return char

    base = ord(char) + step

    return chr((base - ljust) % 26 + (ljust))


def caesar_encode(msg: str, step: int) -> str:
    """
    Encode a string with the caesar cipher
    Args:
        msg: message to be encoded
        step: caesar's step
    Returns:
        str: encoded string
    >>> caesar_encode('abcd', 26)
    'abcd'
    >>> caesar_encode('bdcd', 7)
    'ikjk'
    """
    return "".join(encode_letter(ch, step) for ch in msg)


def decode_letter(char: str, step: int) -> str:
    """
    Decode a single letter from the n-step caesar cipher
    Args:
        char: char to be decoded
        step: caesar's step
    Returns:
        str: decoded char
    >>> decode_letter('j', 26)
    'j'
    >>> decode_letter('j', 28)
    'h'
    """
    ljust = get_ljust(char)
    if ljust == 0:
        return char

    return encode_letter(char, -(abs(step) % 26))


def caesar_decode(msg: str, step: int) -> str:
    """
    Decode a string with the n-step caesar cipher
    Args:
        msg: message to be decoded
        step: caesar's step
    Returns:
        str: decoded string
    >>> caesar_decode('abcd-', 12)
    'opqr-'
    >>> caesar_decode('ijkl', 10)
    'yzab'
    """
    return "".join(decode_letter(char, step) for char in msg)
