"""
picture_decode.py submission
"""

from typing import Dict, List, Tuple


def read_file(path: str) -> Dict[str, List[Tuple[int]]]:
    """
    Parse file from path to dict

    Args:
        path: path to file
    Returns:
        Dict[str, List[Tuple[int]]]: a dictionary with a symbol as a key
        and a list of coordinates of said symbol as items
    >>> read_file("example.txt")
    {'♥': [(0, 0), (1, 1), (2, 2)], '%': [(0, 1), (0, 2), (1, 2)]}
    """
    try:
        with open(path, "r", encoding="utf-8") as infile:
            lst = [line.strip() for line in infile.readlines()]
    except IOError as error:
        print(f"Couldn't read file ({error})")
        raise IOError from error

    output = {}
    for lnum, line in enumerate(lst[0::2]):
        pairs = lst[lnum * 2 + 1].split()
        pairs = list(map(lambda x: (int(x.split("_")[0]), int(x.split("_")[1])), pairs))
        output[line] = pairs
    return output


def save_pict_to_file(symbols: Dict[str, List[Tuple[int]]], textfile: str) -> None:
    """
    Save a picture to file

    Args:
        symbols:  dict the with the same format as read_file returns
        textfile: a path to write to
    >>> save_pict_to_file(read_file('pict.txt'), 'out.txt')
    """
    coords = []

    for _, coord_lst in symbols.items():
        coords.extend(coord_lst)

    width = max(coords, key=lambda x: x[0])[0] + 1
    height = max(coords, key=lambda y: y[1])[1] + 1

    grid = [[" " for _ in range(height)] for y in range(width)]

    for symbol, coord_lst in symbols.items():
        for coord in coord_lst:
            grid[coord[0]][coord[1]] = symbol

    try:
        with open(textfile, "w", encoding="utf-8") as outfile:
            for line in grid:
                outfile.write("".join(line) + "\n")
    except IOError as error:
        print(f"Couldn't write to file ({error})")
        raise IOError from error
