"""
Calculus submission
"""

def find_max_1(func, points):
    """
    (function or str, list(number)) -> (number)

    Find and return maximal value of function f in points.

    >>> find_max_1('x ** 2 + x', [1, 2, 3, -1])
    12
    >>> find_max_1(lambda x: x ** 2 + x, [1, 2, 3, -1])
    12
    """
    if isinstance(func, str):
        mapped_values = map(lambda x: eval(func.replace("x", f"({str(x)})")), points)
    if hasattr(func, '__call__'):
        mapped_values = map(func, points)
    if not mapped_values:
        raise ValueError

    return max(mapped_values)

def find_max_2(func, points):
    """
    (function or str, list(number)) -> (number)

    Find and return list of points where function f has the maximal value.

    >>> find_max_2('x ** 2 + x', [1, 2, 3, -1])
    [3]
    >>> find_max_2(lambda x: x ** 2 + x, [1, 2, 3, -1])
    [3]
    """
    if isinstance(func, str):
        mapped_values = map(lambda x: (x, eval(func.replace("x", f"({str(x)})"))), points)
    elif hasattr(func, '__call__'):
        mapped_values = map(lambda x: (x, func(x)), points)
    else:
        raise ValueError

    max_val = find_max_1(func, points)
    return list(map(lambda x: x[0], filter(lambda x: x[1] == max_val, mapped_values)))

def compute_limit(seq):
    """
    (function or str) -> (number)

    Compute and return limit of a convergent sequence.

    >>> compute_limit('(n ** 2 + n) / n ** 2')
    1.0
    >>> compute_limit(lambda n: (n ** 2 + n) / n ** 2)
    1.0
    """
    i = 0
    lst = []
    while True:
        n = 10 ** i
        if isinstance(seq, str):
            res = eval(seq)
        elif hasattr(seq, '__call__'):
            res = seq(n)
        else:
            raise ValueError
        lst.append(res)
        if i > 1 and abs(lst[i-1] - lst[i-2]) < 0.01 and i < 10**7:
            return round(res, 2)
        i += 1

def compute_derivative(func, x_0):
    """
    (function or str, number) -> (number)

    Compute and return derivative of function f in the point x_0.

    >>> compute_derivative('x ** 2 + x', 2)
    5.0
    >>> compute_derivative(lambda x: x ** 2 + x, 2)
    5.0
    """
    lim = []
    i = 0
    while True:
        dx = 10 ** (-i)
        x = x_0 + dx
        if isinstance(func, str):
            differential = eval(func)
            x = x_0
            differential -= eval(func)
        elif hasattr(func, '__call__'):
            differential = func(x)
            differential -= func(x_0)
        else:
            raise ValueError

        derrivative = differential/dx
        lim.append(derrivative)
        if i > 0 and abs(lim[i] - lim[i - 1]) < 0.001 or i > 10**7:
            return round(derrivative, 2)
        i += 1

def get_tangent(func, x_0):
    """
    (function or str, number) -> (str)

    Compute and return tangent line to function f in the point x_0.

    >>> get_tangent('x ** 2 + x', 2)
    '5.0 * x - 4.0'
    >>> get_tangent('- x ** 2 + x', 2)
    '- 3.0 * x + 4.0'
    >>> get_tangent(lambda x: x ** 2 + x, 2)
    '5.0 * x - 4.0'
    >>> get_tangent(lambda x: - x ** 2 + x, 2)
    '- 3.0 * x + 4.0'
    """
    if isinstance(func, str):
        x = x_0
        val_at_point = eval(func)
    elif hasattr(func, '__call__'):
        val_at_point = func(x_0)
    else:
        raise ValueError
    coefficient = compute_derivative(func, x_0)
    x = f"- {abs(coefficient)} * x" if coefficient < 0 else\
            f"{coefficient} * x"
    free_coeff = round((-1) * x_0 * coefficient + val_at_point, 2)
    formatted_free_coeff = f" - {abs(free_coeff)}" if free_coeff < 0 else\
            f" + {free_coeff}" if free_coeff > 0 else ""
    return x + formatted_free_coeff

def get_root(func, a, b):
    """
    (function or str, number, number) -> (number)

    Compute and return root of the function f in the interval (a, b).

    >>> get_root('x', -1, 1)
    0.0
    >>> get_root(lambda x: x, -1, 1)
    0.0
    """
    val_at_point = 1

    while abs(val_at_point) > 0.01:
        start = (a + b) /2
        if isinstance(func, str):
            x = start
            val_at_point = eval(func)
            x = a
            val_at_a = eval(func)
            x = b
            val_at_b = eval(func)
        elif hasattr(func, '__call__'):
            val_at_point = func(start)
            val_at_a = func(a)
            val_at_b = func(b)
        else:
            raise ValueError
        a = start if (val_at_point*val_at_a) > 0 else a
        b = start if (val_at_point*val_at_b) > 0 else b

    return round(start, 2)
