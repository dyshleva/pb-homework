"""
Sort songs submission
"""
from typing import List, Tuple, Callable, Union


def song_length(song: Tuple[str]) -> float:
    """
    Return aa float from a string pair

    Args:
        song: pair of string

    Returns:
        float: a float of the song's length

    >>> song_length(("1", "1.1"))
    1.1
    """
    return float(song[1])


def title_length(song: Tuple[str]) -> int:
    """
    Return the length of the title

    Args:
        song: pair of string

    Returns:
        int: a int of the song title's length
    >>> title_length(("abc", "a"))
    3
    """
    return len(song[0])


def last_word(song: Tuple[str]) -> str:
    """
    Get the title's last word

    Args:
        song: pair of string

    Returns:
        str: the song's last word
    >>> last_word(("aab bs", "a"))
    'bs'
    """
    return str(song[0].split()[-1])


def sort_songs(
    song_titles: List[str],
    length_songs: List[str],
    key: Callable[[tuple], Union[int, str, float]],
) -> List[Tuple]:
    """
    Sort songs by song title list, length and key
    >>> sort_songs(["a", "b", "ab"], ["1.1", "6.06", "3.02"], song_length)
    [('a', '1.1'), ('ab', '3.02'), ('b', '6.06')]
    """
    if len(song_titles) != len(length_songs):
        return None
    for _ in song_titles + length_songs:
        if not isinstance(_, str):
            return None

    return list(sorted(zip(song_titles, length_songs), key=key))
