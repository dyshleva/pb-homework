from itertools import combinations

def cross_product(points: [(float, float)]) -> float:
    """
    Get the cross-product of two vectors

    Args:
        points: list of points

    Returns:
        float: the cross-product
    """

    x1 = (points[1][0] - points[0][0])
    y1 = (points[1][1] - points[0][1])
    x2 = (points[2][0] - points[0][0])
    y2 = (points[2][1] - points[0][1])

    return x1*y2 - x2*y1

def is_convex(*points: [(float, float)]) -> bool:
    """
    Check if polygon is convex
    Args:
        points: list of points tht are the vertices of the polygon

    Returns:
        bool: a boolen that corresponds to the polygon's convexness
    """
    prev = 0
    cur = 0
    print(points)
    for i in range(len(points)):
        tmp = [points[0][i],
               points[0][(i+1) % len(points)],
               points[0][(i+2) % len(points)]]

        cur = cross_product(tmp)

        if cur * prev < 0:
            return False
        prev = cur

    return True

def four_lines_area(k1: float, c1: float,
  k2: float, c2: float,
  k3: float, c3: float,
  k4: float, c4: float) -> float:
    """
    Get the area of a four line intersection quadriliteral
    Args:
        k1-4: line coefficients
        c1-4: free coefficients

    Returns:
        A quadriliteral area
    """

    pairs = [(k1, c1), (k2, c2), (k3,c3), (k4,c4)]

    intersects = [
      lines_intersection(*cartesian_pair[0], *cartesian_pair[1])
      for cartesian_pair in list(
        filter(lambda x: x[0]!=x[1], [(x, y) for x in pairs for y in pairs])
        )
    ]

    intersects = list(filter(lambda x: x is not None, intersects))

    combs = []
    for i in intersects:
        if i not in combs:
            combs.append(i)

    combs = list(combinations(combs, 4))

    combs = list(filter(lambda x: is_convex(list(x)), combs))

    areas = list(quadrangle_area(*sorted([
            distance(*points[i], *points[j])
            for i,j in [(0, 1), (1, 2), (2, 3), (3, 0), (0, 2), (1, 3)]
            ])) for points in combs)

    return round(max(areas), 2)

def lines_intersection(k1: float, c1: float,
  k2: float, c2: float
  ) -> (float, float):
    """
    Get the intersection of the lines.
    If the lines are parralel, returns None

    Args:
        k1-k2: coefficients in line equations
        c1-2: free coefficients in line equations
    Returns:
        (float, float): a pait of coordinapes
    """
    if k1 == k2:
        return None

    x = (c2 - c1) / (k1 - k2)
    y = k1*x + c1

    return round(x, 2), round(y, 2)


def distance(x1: float, y1: float, x2: float, y2: float) -> float:
    """
    Get distance between points

    Args:
        x1-2: x coordinates
        y1-2: y coordinates

    Returns:
        distance between two points
    """
    return round(((x1 -x2) ** 2 + (y1 - y2) ** 2) ** 0.5, 2)

def quadrangle_area(a: float=0, b: float=0,
  c: float=0, d: float=0, f1: float=0, f2: float=0) -> float:
    """
    Get area of a quadrangle shape

    Args:
        a-d: sides
        f1-2: diagonals
    """
    area_squared = 4*(f1**2)*(f2**2) - ((b**2 + d**2 - c**2 - a**2)**2)
    area_squared /= 16

    if area_squared<0:
        return 0

    return round(area_squared ** 0.5, 2)
