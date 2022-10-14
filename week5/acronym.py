"""
The acronym submission
"""


def create_acronym(phrases: str) -> str:
    """
    Create acronyms of phrases
    Args:
        phrases: phrases separated by newlines
    Returns:
        str: acronyms
    >>> create_acronym("random access memory\\nAs soon As possible")
    'RAM - random access memory\\nASAP - As soon As possible'
    >>> create_acronym("random access memory")
    'RAM - random access memory'
    """
    lines = phrases.split("\n")
    acronyms = ["".join(word[0].upper() for word in line.split()) for line in lines]
    result = "\n".join(" - ".join(pair) for pair in zip(acronyms, lines))
    return result
