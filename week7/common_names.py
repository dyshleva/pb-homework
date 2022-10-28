"""
Common names submission
"""
from typing import List, Set

VOWELS = "AEIOU"


def names_read(file_name: str) -> Set[str]:
    """
    Reads a file and returns a set of it's lines

    Args:
        file_name: file to read

    Returns:
        Set[str]: a set of the file's lines
    """
    with open(file_name, "w", encoding="utf-8") as infile:
        set = {name.strip() for name in infile.read().split("\n")}
    return set


def common_names(female_names: List[str], male_names: List[str]) -> Set[str]:
    """
    Returns an intersection of two lists

    Args:
        female_names: first list of strings
        male_names: second list of strings
    Returns:
        Set[str]: a sey intersection of two lists

    >>> common_names(["Anna", "Irene", "Bellamy"], ["Bellamy", "John"])
    {'Bellamy'}
    """

    return set(
        filter(
            lambda name: any(name.upper().startswith(vowel) for vowel in VOWELS),
            set(female_names).intersection(set(male_names)),
        )
    )


def main():
    """
    The main function
    """
    male_set = names_read("male.txt")
    female_set = names_read("female.txt")

    print(common_names(list(male_set), list(female_set)))


if __name__ == "__main__":
    main()
