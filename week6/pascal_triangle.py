"""
Pascal triangle submission
"""


def generate_pascal_triangle(height: int) -> list[int]:
    """
    Generate a pacsal triangle

    Args:
        height: the triangle's height
    Returns:
        list[int]: a list tht represents the pascal triangle
    >>> generate_pascal_triangle(1)
    [[1]]
    >>> generate_pascal_triangle(5)
    [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    """
    base = [[1], [1, 1]]

    if height <= 2:
        return base[:height]

    for i in range(1, height - 1):
        new_lst = [1]

        for j in range(1, len(base[i])):
            new_lst.append(base[i][j] + base[i][j - 1])

        new_lst += [1]
        base.append(new_lst)

    return base
