"""
Lab work for discrete maths
"""

from copy import deepcopy

def symmetric_closure(init: list[list[int]]) -> list[list[int]]:
    """
    Make a symmetric closure of a boolean atrix

    Args:
        init: a square boolean (int) matrix

    Returns:
        list[list[int]]: a square boolean (int) matrix
    """
    assert all(len(init) == len(x) for x in init)
    res = deepcopy(init)
    for i in range(len(res)):
        for j in range(len(res)):
            res[i][j] = res[i][j] or res[j][i]

    return res

def reflexive_closure(init: list[list[int]]) -> list[list[int]]:
    """
    Make a reflexive closure of a boolean atrix

    Args:
        init: a square boolean (int) matrix

    Returns:
        list[list[int]]: a square boolean (int) matrix
    """
    assert all(len(init) == len(x) for x in init)
    res = deepcopy(init)
    for i in range(len(res)):
        for j in range(len(res)):
            res[i][j] = res[i][j] or int(i == j)

    return res

def transitive_closure(init: list[list[int]]) -> list[list[int]]:
    """
    Warshall algorithm implementation for a square matrix

    Args:
        init: a square boolean (int) matrix

    Returns:
        list[list[int]]: a square boolean (int) matrix
    """
    assert all(len(init) == len(x) for x in init)
    res = deepcopy(init)
    for k in range(len(res)):
        for i in range(len(res)):
            for j in range(len(res)):
                res[i][j] = res[i][j] or (res[i][k] and res[k][j])

    return res

def transitive_check(matrix: list[list[int]]) -> list[list[int]]:
    """
    Check matrix for it's transitivity

    Args:
        matrix: a square boolean matrix to bo checked

    Returns:
        bool: whether a matrix is transitive
    """
    assert all(len(init) == len(x) for x in init)
    res = deepcopy(matrix)
    res = transitive_closure(res)
    for i in range(len(res)):
        for j in range(len(res)):
            if res[i][j] == 1 and matrix[i][j] == 0:
                return False
    return True
