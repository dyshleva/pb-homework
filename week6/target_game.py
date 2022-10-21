"""
Target game submission
"""

from typing import List
from string import ascii_uppercase
from random import choice


def generate_grid() -> List[List[str]]:
    """
    Generates list of lists of letters - i.e. grid for the game.
    e.g. [['I', 'G', 'E'], ['P', 'I', 'S'], ['W', 'M', 'G']]
    """
    grid = [["" for _ in range(3)] for __ in range(3)]
    i = 0
    j = 0
    while not all(x != "" for row in grid for x in row):
        while not all(x != "" for x in grid[i]):
            letter = choice(ascii_uppercase)
            if not any(letter in row for row in grid):
                grid[i][j] = letter
                j += 1
        j = 0
        i += 1

    return grid


def get_words(infile: str, letters: List[str]) -> List[str]:
    """
    Reads the file infile. Checks the words with rules and returns a list of words.
    """
    lst = []
    center = letters[4]
    with open(infile, "r", encoding="utf-8") as file:
        for line in file:
            flag = len(line.strip()) >= 4 and\
                center in line.strip() and\
                line.strip() not in lst

            for letter in line.strip():
                flag = letter in letters and line.strip().count(letter) == 1 and flag

            if flag and line.strip():
                lst.append(line.strip())

    return sorted(lst)


def get_user_words() -> List[str]:
    """
    Gets words from user input and returns a list with these words.
    Usage: enter a word or press ctrl+d to finish.
    """
    lst = []
    while (inp := input()) != "":
        lst.append(inp)
    return lst


def get_pure_user_words(
    user_words: List[str], letters: List[str], words_from_dict: List[str]
) -> List[str]:
    """
    (list, list, list) -> list

    Checks user words with the rules and returns list of those words
    that are not in dictionary.
    """
    result = []
    center = letters[4]
    for word in user_words:
        flag = len(word) >= 4 and\
                center in word and\
                not word in words_from_dict and\
                not word in result
        for letter in word:
            flag = letter in letters and word.count(letter) == 1 and flag

        if flag:
            result.append(word)

    return result


def results():
    """
    The game function
    """
    letters = ''.join(''.join(x) for x in generate_grid()).lower()
    print("""
Welcome to the target game!
Please enter all the words you ca think of that consist of thos letters:
""")
    print(letters)
    words = get_user_words()
    file_words = get_words("en", letters)
    pure_words = get_pure_user_words(words, letters, file_words)

    print("Yay! you've entered the words! Here are all the words you got from the dictionary:")
    print("\n".join(map(lambda x: f"- {x}", pure_words)))
    print("And here's all the possible words from the dictionary")
    print("\n".join(file_words))
    with open('result.txt', 'w', encoding='utf-8') as outfile:
        outfile.writelines(pure_words)
