"""
Lab work for discrete maths
"""

from copy import deepcopy
from itertools import combinations

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
    for i in range(matrix_size):
        for j in range(matrix_size):
            for k in range(matrix_size):
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
    assert all(len(matrix) == len(x) for x in matrix) and matrix is not None
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
    assert all(len(matrix) == len(x) for x in matrix) and matrix is not None
    matrix_size = len(matrix)
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
    assert all(len(matrix) == len(x) for x in matrix) and matrix is not None
    matrix_size = len(matrix)
    for i in range(matrix_size):
        for j in range(matrix_size):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True

def equivalence_class(matrix: list[list[int]]) -> dict[str: list[int]]:
    """
    Create a dictionaary with equivalence classes

    Args:
        matrix: a boolean (int) matrix

    Returns:
        dict[str: list[int]]: a dictionary with the equivalenc elist turned to string as a key,
            and list of matric row indexes as objects
    """
    matrix = transitive_closure(symmetric_closure(reflexive_closure(matrix)))
    result = [[it for it, el in enumerate(row) if el] for row in matrix]
    return set(result)

def bruteforce_transitives(set_length: int) -> int:
    """
    Calculate all possible transitive relations for a set with n elements
    Sowwy, nothing but bruteforce works

    Args:
        set_length: length of the said set

    Returns:
        int: number of all possible transitive relations
    """
    cartesian = [(x, y) for x in range(set_length) for y in range(set_length)]

    relations = []

    for i in range(len(cartesian)+1):
        for comb in combinations(cartesian, i):
            relations.append(list(comb))

    matrixes = []
    for i in relations:
        matrix = [[0 for i in range(set_length)] for j in range(set_length)]
        for x, y in i:
            matrix[x][y] = 1
        matrixes.append(matrix)

    result = []

    for matrix in matrixes:
        if transitive_check(matrix) and matrix not in result:
            result.append(matrix)

    return len(matrixes)

def read_file(file_name: str) -> list[list[int]]:
    with open(file_name, "r") as file:
        matrix = [[int(char) for char in row.strip()] for row in file.readlines()]
    return matrix

def write_file(file_name: str, matrix: list[list[int]]) -> None:
    with open(file_name, "w") as infile:
        infile.writelines(''.join(row) for row in matrix)