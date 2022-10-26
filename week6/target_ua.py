"""
Target game submission
"""

from typing import List, Tuple
import re
from random import choice

ua_alphabet = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя"

def generate_grid() -> List[List[str]]:
    """
    Generates list of lists of letters - i.e. grid for the game.
    """
    grid = "     "
    i = 0
    while not all(x != " " for x in grid):
        letter = choice(ua_alphabet)
        if not any(letter in row for row in grid):
            grid[i] = letter
        i += 1

    return grid


def get_words(infile: str, letters: List[str]) -> List[Tuple[str]]:
    """
    Reads the file infile. Checks the words with rules and returns a list of words.
    """
    lst = []
    center = letters[len(letters)//2]
    with open(infile, "r", encoding="utf-8") as file:
        for line in file:
            flag = line.strip() and\
                    len(line.strip().split()[0]) <= 5 and\
                    line[0] in letters

            part = ''

            if re.match('.*(/n)|(noun).*', line):
                part = 'noun'
            if re.match('.*(/v)|(verb).*', line):
                part = 'verb'
            if re.match('.*(/adj).*', line):
                part = 'adjective'
            if re.match('.*(adv).*', line):
                part = 'adverb'
            if flag and part:
                lst.append((line.strip().split[0], part))

    return lst

def get_user_words() -> List[str]:
    """
    Gets words from user input and returns a list with these words.
    Usage: enter a word or press ctrl+d to finish.
    """
    lst = []
    while (inp := input()) != "":
        lst.append(inp)
    return lst


def check_user_words(
        user_words: List[str], language_part: str,
        letters: List[str], dict_of_words: List[Tuple[str]]
) -> Tuple[List[str]]:
    """
    (list, str, list, list) -> list

    Checks user words with the rules and returns list of those words
    """
    result = []
    center = letters[4]
    proper_words = [word[0] if word[1] == language_part for word in dict_of_words]
    for word in user_words:
        flag = len(word) <= 5 and\
                center in word and\
                not word in result and\
                word in proper_words

        if word in proper_words:
            proper_words.remove(word)

        for letter in word:
            flag = letter in letters and word.count(letter) == 1 and flag

        if flag:
            result.append(word)

    return result, proper_words


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
