"""
expression_calculator submission.
I could build a recursive finite coalgebra representing
a decision tree, but I'm too lazy, so you get a terrible list-popping
algorithm that takes O(NlogN)
"""

def calculate_expression(expression):
    """
    (str) -> int|str
    Calculate an expression

    Args:
        expression: strng to be evaluateg
    Returns:
        int: the result
        str: 'Неправильний вираз!' if the exptression is faulty
    >>> calculate_expression("Скільки буде 8 відняти 3?")
    5
    >>> calculate_expression("Скільки буде 7 додати 3 помножити на 5?")
    50
    >>> calculate_expression("Скільки буде 10 поділити на -2 додати 11 мінус -3?")
    9
    >>> calculate_expression("Скільки буде 3 в кубі?")
    'Неправильний вираз!'
    """
    ops = {"додати": lambda x,y: x+y,
           "плюс": lambda x,y: x+y,
           "відняти": lambda x,y: x-y,
           "мінус": lambda x,y: x-y,
           "помножитина": lambda x,y: x*y,
           "поділитина": lambda x,y: x/y}

    expr = expression.replace("помножити на", "помножитина")
    expr = expr.replace("поділити на", "поділитина")
    expr = expr.replace("?", "")

    if not expr.startswith("Скільки буде"):
        return "Неправильний вираз!"

    expr = expr.replace("Скільки буде ", "")
    expr = expr.split()

    try:
        number_queue = [int(i) for i in expr[::2]]
    except ValueError:
        return "Неправильний вираз!"

    op_queue = expr[1::2]
    for op in op_queue:
        if ops.get(op) is None:
            return "Неправильний вираз!"

    while op_queue and len(number_queue) > 1:
        try:
            cur = ops[op_queue[0]](number_queue[0], number_queue[1])
            number_queue.pop(0)
            number_queue.pop(0)
            number_queue.insert(0, cur)
            op_queue.pop(0)
        except ValueError:
            return "Неправильний вираз!"
        except ZeroDivisionError:
            return "Неправильний вираз!"


    return int(number_queue[0])
