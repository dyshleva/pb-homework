"""
Cmudict submission
"""
from typing import Dict, List, Tuple, Set


def dict_reader_tuple(file_dict: str) -> List[Tuple[str]]:
    """
    Read a file into a list of tuples
    Args:
        file_dict: filename to read from
    Returns:
        List[Tuple[str]]: list of tuples
    """
    with open(file_dict, "r", encoding="utf-8") as infile:
        tuples = [
            (
                line.strip().split()[0],
                int(line.strip().split()[1]),
                line.strip().split()[2:],
            )
            for line in infile.readlines()
        ]
    return tuples


def dict_reader_dict(file_dict: str) -> Dict[str, Set[Tuple[str]]]:
    """
    Read dictionary file as a dict
    Args:
        file_dict: filename

    Returns:
        Dict[str, Str[Tuple[str]]]: a dict with words as keys and pronounciations as elements
    """
    tuples = {}
    with open(file_dict, "r", encoding="utf-8") as infile:
        for line in infile.readlines():
            if line.strip().split()[0] in tuples:
                tuples[line.strip().split()[0]].add(tuple(line.strip().split()[2:]))
            else:
                tuples[line.strip().split()[0]] = {tuple(line.strip().split()[2:])}
    return tuples


def list_to_dict(lst):
    """
    Makes a proper dict out of the first format
    """
    result = {}
    for pron in lst:
        if pron[0] in result:
            result[pron[0]].add(tuple(pron[2]))
        else:
            result[pron[0]] = {tuple(pron[0])}
    return result


def dict_invert(dct):
    """
    Man, i'm not writing documentation for this
    >>> dict_invert({'WATER':{('W','A','T','E','R')}})
    {1: {('WATER', ('W', 'A', 'T', 'E', 'R'))}}
    """
    base = dct
    result = {}
    if isinstance(dct, list):
        base = list_to_dict(dct)
    if isinstance(base, dict):
        for word, prons in base.items():
            if len(prons) in result:
                for pron in prons:
                    result[len(prons)].add((word, pron))
            else:
                result[len(prons)] = set()
                for pron in prons:
                    result[len(prons)].add(tuple([word, pron]))
    return {key: result[key] for key in sorted(result.keys())}
