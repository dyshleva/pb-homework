
# Complete all of the following functions. Currently they all just
# 'pass' rather than explicitly return value, which means that they
# implicitly return None.
"""
I dislike the fact that i have to make a new repo for every task
"""
from typing import List, Dict, Tuple


def get_graph_from_file(file_name: str) -> List[List[int]]:
    """
    (str) -> (list)
    Read graph from file and return a list of edges.
    Args:
        file_name: the filename

    Returns:
        List[List[int]] - list of edges
    >>> get_graph_from_file("data1.txt")
    [[1, 2], [3, 4], [1, 5]]
    """
    with open(file_name, "r", encoding="utf-8") as infile:
        graph_edges = [
            [int(edge) for edge in line.split(",")[0:2]] for line in infile.readlines()
        ]
    return graph_edges


def to_edge_dict(edge_list: List[List[int]]) -> Dict[int, List[int]]:
    """
    (list) -> (dict)

    Convert a graph from list of edges to dictionary of vertices.

    Args:
        edge_list: lsit of edges

    Returns:
        Dict[int, List[int]]: a dict with nodes as keys and list of nodes as present edges

    >>> to_edge_dict([[1, 2], [3, 4], [1, 5], [2, 4]])
    {1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}
    """
    result = {}
    for pair in edge_list:
        if pair[0] in result:
            result[pair[0]].append(pair[1])
        else:
            result[pair[0]] = [pair[1]]
        if pair[1] in result:
            result[pair[1]].append(pair[0])
        else:
            result[pair[1]] = [pair[0]]
    for _, edges in result.items():
        edges.sort()
    return result


def is_edge_in_graph(graph: Dict[int, List[int]], edge: Tuple[int]) -> bool:
    """
    (dict, tuple) -> bool

    Return True if graph contains a given edge and False otherwise.

    Args:
        graph: dict representation of a graph
        edge: tuple of two nodes
    Returns:
        bool: whether an edge exists in the graph

    >>> is_edge_in_graph({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, (3, 1))
    False
    """
    return edge[0] in graph and edge[1] in graph[edge[0]]


def add_edge(graph: Dict[int, List[int]], edge: Tuple[int]) -> Dict[int, List[int]]:
    """
    (dict, tuple) -> dict

    Add a new edge to the graph and return new graph.

    Args:
        graph: dict representation of a graph
        edge: a new edge to add
    Returns:
        Dict[int, List[int]]: a new graph

    >>> add_edge({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, (1, 3))
    {1: [2, 5, 3], 2: [1, 4], 3: [4, 1], 4: [2, 3], 5: [1]}
    """
    if edge[0] in graph:
        graph[edge[0]].append(edge[1])
    else:
        graph[edge[0]] = [edge[1]]

    if edge[1] in graph:
        graph[edge[1]].append(edge[0])
    else:
        graph[edge[1]] = [edge[0]]
    return graph


def del_edge(graph: Dict[int, List[int]], edge: Tuple[int]) -> Dict[int, List[int]]:
    """
    (dict, tuple) -> (dict)

    Delete an edge from the graph and return a new graph.

    Args:
        graph: dict representation of a graph
        edge: an edge to delete
    Returns:
        Dict[int, List[int]]: a new graph


    >>> del_edge({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, (2, 4))
    {1: [2, 5], 2: [1], 3: [4], 4: [3], 5: [1]}
    """
    if edge[0] in graph and edge[1] in graph[edge[0]]:
        graph[edge[0]].remove(edge[1])
    if edge[1] in graph and edge[0] in graph[edge[1]]:
        if edge[0] in graph[edge[1]]:
            graph[edge[1]].remove(edge[0])
    return graph


def add_node(graph: Dict[int, List[int]], node: int) -> Dict[int, List[int]]:
    """
    (dict, int) -> (dict)

    Add a new node to the graph and return a new graph.

    Args:
        graph: dict representation of a graph
        node: new node to add
    Returns:
        Dict[int, List[int]]: a new graph

    >>> add_node({1: [2], 2: [1]}, 3)
    {1: [2], 2: [1], 3: []}
    """
    if node not in graph:
        graph[node] = []
    return graph


def del_node(graph: Dict[int, List[int]], node: int) -> Dict[int, List[int]]:
    """
    (dict, int) -> (dict)

    Delete a node and all incident edges from the graph.

    Args:
        graph: dict representation of a graph
        node: node to delete
    Returns:
        Dict[int, List[int]]: a new graph

    >>> del_node({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, 4)
    {1: [2, 5], 2: [1], 3: [], 5: [1]}
    """
    if node in graph:
        graph.pop(node)
    for dict_node, edges in graph.items():
        if node in edges:
            graph[dict_node].remove(node)
    return graph


def convert_to_dot(graph: Dict[int, List[int]]) -> None:
    """
    (dict) -> (None)

    Save the graph to a file in a DOT format.
    Args:
        graph: dict representation of a graph
    """
    result = "graph {\n"
    for node, edges in graph.items():
        result += f"{node};\n"
        for edge in edges:
            result += f"    {node} -- {edge};\n"
    result += "}"
    with open("graph.dot", "w", encoding="utf-8") as outfile:
        outfile.write(result)
