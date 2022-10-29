"""
crossword.py submission
"""

from typing import List, Tuple


def read_crossword(path: str) -> List[Tuple[str, Tuple[int]]]:
    """
    Read a crossword form a list

    Args:
        path: path to file

    Returns:
        List[Tuple[str, Tuple[int]]]: a list of tuples of chars and coordinates
    """
    lst = []
    with open(path, "r", encoding="utf-8") as infile:
        lines = infile.readlines()
    for line in lines:
        line = line.strip()
        char = line[0]
        coords = line[1:]
        for i in range(0, len(coords), 2):
            lst.append((char, (int(coords[i]), int(coords[i + 1]))))
    return lst


def find_words(crossword: List[Tuple[str, Tuple[int]]], length: int) -> List[str]:
    """
    Find the horizontal words of given length in crossword

    Args:
        crossword: a crossword in the format described above
        length: length of word
    Returns:
        List[str]: the words
    """
    lines = [[" " for _ in range(10)] for __ in range(10)]

    for coordinate in crossword:
        lines[coordinate[1][1]][coordinate[1][0]] = coordinate[0]

    lines = list(map(lambda x: str.join("", x), lines))

    result = []

    for line in lines:
        for word in line.split():
            if len(word) == length:
                result.append(word)
    return result
