"""
dyvo_insert assignment
"""


def dyvo_insert(sentence, flag):
    """
    Insert диво before every word in sentence
    if it begins with flag
    Args:
        sentence: string to be edited
        flag: letters, with which the word that will have dyvo before it
    Returns:
        str: the edited string
    >>> dyvo_insert("hello there!", "hello")
    'дивоhello there!'
    >>> dyvo_insert("hello there!", "th")
    'hello дивоthere!'
    """
    res = ""

    for word in sentence.split():
        res += f" диво{word} " if word.lower().startswith(flag) else f" {word} "

    return " ".join(res.split())
