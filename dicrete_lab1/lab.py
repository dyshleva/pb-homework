"""
Lab work for discrete maths
"""

from copy import deepcopy

def symmetric_closure(init: list[list[int]] = None) -> list[list[int]]:
    """
    Make a symmetric closure of a boolean atrix

    Args:
        init: a square boolean (int) matrix

    Returns:
        list[list[int]]: a square boolean (int) matrix
    """
    assert all(len(init) == len(x) for x in init) and init is not None
    res = deepcopy(init)
    matrix_size = len(res)
    for i in range(matrix_size):
        for j in range(matrix_size):
            res[i][j] = res[i][j] or res[j][i]

    return res

def reflexive_closure(init: list[list[int]] = None) -> list[list[int]]:
    """b
    Make a reflexive closure of a boolean atrix

    Args:
        init: a square boolean (int) matrix

    Returns:
        list[list[int]]: a square boolean (int) matrix
    """
    assert all(len(init) == len(x) for x in init) and init is not None
    res = deepcopy(init)
    matrix_size = len(res)
    for i in range(matrix_size):
        res[i][i] = 1

    return res

def transitive_closure(init: list[list[int]] = None) -> list[list[int]]:
    """
    Warshall algorithm implementation for a square matrix

    Args:
        init: a square boolean (int) matrix

    Returns:
        list[list[int]]: a square boolean (int) matrix
    """
    assert all(len(init) == len(x) for x in init) and init is not None
    res = deepcopy(init)
    matrix_size = len(res)
    for k in range(matrix_size):
        for i in range(matrix_size):
            for j in range(matrix_size):
                res[i][j] = res[i][j] or (res[i][k] and res[k][j])

    return res

def transitive_check(matrix: list[list[int]] = None) -> list[list[int]]:
    """
    Check matrix for it's transitivity

    Args:
        matrix: a square boolean matrix to bo checked

    Returns:
        bool: whether a matrix is transitive
    """
    assert all(len(init) == len(x) for x in init) and init is not None
    res = deepcopy(matrix)
    res = transitive_closure(res)
    return res == matrix

def reflexive_check(matrix: list[list[int]] = None) -> list[list[int]]:
    """
    Check matrix for it's reflexiveness

    Args:
        matrix: a square boolean matrix to bo checked

    Returns:
        bool: whether a matrix is reflexive
    """
    assert all(len(init) == len(x) for x in init) and init is not None
    matrix_size = len(res)
    for i in range(matrix_size):
        if not matrix[i][i]:
            return False
    return True

def symmetric_check(matrix: list[list[int]] = None) -> list[list[int]]:
    """
    Check matrix for it's symmetry

    Args:
        matrix: a square boolean matrix to bo checked

    Returns:
        bool: whether a matrix is symmetric
    """
    assert all(len(init) == len(x) for x in init) and init is not None
    matrix_size = len(res)
    for i in range(matrix_size):
        for j in range(matrix_size):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True
