"""
Keyword submission
"""


def find_film_keywords(film_keywords: dict, film_name: str) -> set:
    """
    Find keywords that the film_name contains
    (we go the other way: dict has keywords for keys and film name sets for items)

    Args:
        film_keywords: dict of keywords aand sets of film names
        film_name: film name
    Returns:
        set: a set of keywords
    >>> find_film_keywords({"abandon": {"abandon-ship", "abandoned-by-boyfriend"},\
"bomb": {"a-bomb"}}, "abandon-ship")
    {'abandon'}
    """
    result_keywords = filter(lambda item: film_name in item[1], film_keywords.items())
    result = set(map(lambda item: item[0], result_keywords))
    return result


def find_films_with_keywords(film_keywords: dict, num_of_films: int) -> list:
    """
    Finds a list of films with most keywords

    Args:
        film_keywords: dict of keywords as keys and sets of film names as items
        num_of_films:length of the list
    Returns:
        list of typles, where the first element is the film name, and the
        second one is the number of keywords in it
    >>> len(find_films_with_keywords({"abandon": {"abandon-ship", "abandoned-by-boyfriend"},\
"bomb": {"a-bomb"}}, 2))
    2
    """
    result = {}
    for key, films in film_keywords.items():
        for film in films:
            if film in result:
                result[film].append(key)
            else:
                result[film] = [key]
    result = result.items()
    result = sorted(
        map(lambda x: (x[0], len(x[1])), result), key=lambda x: x[1], reverse=True
    )

    return result[0:num_of_films]
