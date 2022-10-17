"""
Lab work for discrete maths
"""

from copy import deepcopy
from dataclasses import dataclass
from typing import Generator
from functools import partial
from operator import add

@dataclass
class Matrix:
    data: list[list[int]]

    def __post_init__(self) -> None:
        """
        Post init. Assert whether the matrix is square
        """
        assert all(len(self.data) == len(x) for x in self.data)

    @property
    def size(self) -> int:
        return len(self.data)

    def copy(self) -> "Matrix":
        return deepcopy(self)

    def __getitem__(self, item: tuple[int, int]) -> int:
        x, y = item
        return self.data[x][y]

    def __setitem__(self, item: tuple[int, int], val: int) -> None:
        x, y = item
        self.data[x][y] = val

    def __iter__(self) -> Generator[list[int], None, None]:
        yield from self.data

    def enum(self, depth=2):
        if depth == 1:
            yield from map(lambda x: (x,), range(self.size))
            return
        for i in self.enum(1):
            yield from map(partial(add, i), self.enum(depth - 1))


def symmetric_closure(init: Matrix) -> Matrix:
    """
    Make a symmetric closure of a boolean atrix

    Args:
        init: a square boolean (int) matrix

    Returns:
        list[list[int]]: a square boolean (int) matrix
    """
    res = init.copy()
    for i in range(res.size):
        for j in range(res.size):
            res[i, j] = res[i, j] or res[j, i]

    return res

def reflexive_closure(init: Matrix) -> Matrix:
    """
    Make a reflexive closure of a boolean atrix

    Args:
        init: a square boolean (int) matrix

    Returns:
        list[list[int]]: a square boolean (int) matrix
    """
    res = init.copy()
    for i in range(res.size):
        for j in range(res.size):
            res[i, j] = res[i, j] or i == j

    return res

def transitive_closure(init: Matrix) -> Matrix:
    """
    Warshall algorithm implementation for a square matrix

    Args:
        init: a square boolean (int) matrix

    Returns:
        list[list[int]]: a square boolean (int) matrix
    """
    res = init.copy()
    for k in range(res.size):
        for i in range(res.size):
            for j in range(res.size):
                res[i, j] = res[i, j] or (res[i, k] and res[k, j])

    return res

def transitive_check(matrix: Matrix) -> Matrix:
    """
    Check matrix for it's transitivity

    Args:
        matrix: a square boolean matrix to bo checked

    Returns:
        bool: whether a matrix is transitive
    """
    res = matrix.clone()
    res = transitive_closure(res)
    for i in range(res.size):
        for j in range(res.size):
            if res[i, j] == 1 and matrix[i, j] == 0:
                return False
    return True
