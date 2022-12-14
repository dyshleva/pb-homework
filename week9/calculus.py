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
        mapped_values = map(lambda num: eval(func.replace("x", f"({str(num)})")), points)
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
        mapped_values = map(lambda num: (num, eval(func.replace("x", f"({str(num)})"))), points)
    elif hasattr(func, '__call__'):
        mapped_values = map(lambda num: (num, func(num)), points)
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
        num = 10 ** i
        if isinstance(seq, str):
            res = eval(seq.replace("n", "num"))
        elif hasattr(seq, '__call__'):
            res = seq(num)
        else:
            raise ValueError
        lst.append(res)
        if i > 1 and abs(lst[i-1] - lst[i-2]) < 0.001 or i > 10**7:
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
        diff_x = 10 ** (-i)
        point = x_0 + diff_x
        if isinstance(func, str):
            differential = eval(func.replace("x", "point"))
            point = x_0
            differential -= eval(func.replace("x", "point"))
        elif hasattr(func, '__call__'):
            differential = func(point)
            differential -= func(x_0)
        else:
            raise ValueError

        derrivative = differential/diff_x
        lim.append(derrivative)
        if 10**7 > i > 0 and abs(lim[i] - lim[i - 1]) < 0.001 or i > 10**7:
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
        val_at_point = eval(func.replace("x", "point"))
    elif hasattr(func, '__call__'):
        val_at_point = func(x_0)
    else:
        raise ValueError
    coefficient = compute_derivative(func, x_0)
    line = f"- {abs(coefficient)} * x" if coefficient < 0 else\
            f"{coefficient} * x"
    free_coeff = round((-1) * x_0 * coefficient + val_at_point, 2)
    formatted_free_coeff = f" - {abs(free_coeff)}" if free_coeff < 0 else\
            f" + {free_coeff}" if free_coeff > 0 else ""
    return line + formatted_free_coeff

def get_root(func, fst, snd):
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
        start = (fst + snd) /2
        if isinstance(func, str):
            val_at_point = eval(func.replace("x", "start"))
            val_at_fst = eval(func.replace("x", "fst"))
            val_at_snd = eval(func.replace("x", "snd"))
        elif hasattr(func, '__call__'):
            val_at_point = func(start)
            val_at_fst = func(fst)
            val_at_snd = func(snd)
        else:
            raise ValueError
        fst = start if (val_at_point*val_at_fst) > 0 else fst
        snd = start if (val_at_point*val_at_snd) > 0 else snd

    return round(start, 2)
