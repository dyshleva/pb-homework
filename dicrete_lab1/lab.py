"""
Lab work for discrete maths
"""


def filter_by(key, functor, lst):
    """
    (b, ((a -> b) ⇒ [a])) ⇒ [a]
    Filter list of pairs into list of objects, grouped by key

    Args:
        key: key to be filtered with
        functor: function from pair to object (fst or snd or some conversion)
                 (it IS a functor tbh)
        lst: list of pairs

    Returns:
        [a]: list of objects
    >>> filter_by(1, lambda x: x[0], [(1, 1), (1, 2), (2, 3)])
    [(1, 1), (1, 2)]
    >>> filter_by(1, lambda x: x[1], [(1, 1), (1, 2), (3, 1)])
    [(1, 1), (3, 1)]
    """
    return list(filter(lambda x: functor(x) == key, lst))


def combine(lst_fst, lst_snd):
    """
    ([(a,b)], [(b,c)]) ⇒ [([a], [c])]
    Combine two lists with filter_by

    Args:
        lst_fst: list of type [(a,b)]
        lst_snd: list of type [(b,c)]

    Returns:
        [([a], [c])]: list of pairs of lists, such that
                      ∀ ([a], [c]) ϵ [([a], [c])]
                      ∀ a₁, c₁ ϵ ([a], [c])
                      ∃ b₁ : (a₁, b₁) ϵ [(a, b)] and (b₁, c₁) ϵ [(b, c)]
    >>> combine([(1, 1), (2, 2)], [(1,2), (2, 1)])
    [([1], [1]), ([2], [2])]
    """
    return [
        (
            [pair_fst[0] for pair_fst in filter_by(key, lambda pair: pair[1], lst_fst)],
            [pair_snd[1] for pair_snd in filter_by(key, lambda pair: pair[0], lst_snd)],
        )
        for key in {pair[1] for pair in lst_fst}
    ]


def cartesian(lst_fst, lst_snd):
    """
    Make a cartesian product of two lists
    Args:
        lst_fst: first list
        lst_snd: second list
    Returns:
        list: a cartesian product of two lists
    >>> cartesian([1,2], [1])
    [(1, 1), (2, 1)]
    """
    return [(x, y) for x in lst_fst for y in lst_snd]


def compose(lst_fst, lst_snd):
    """
    ([(a,b)], [(b,c)]) ⇒ [(a,c)]
    Compose two relations in the representation of the list of pairs

    Args:
        lst_fst: first relation
        lst_snd: second_relation

    Returns:
        [(a, c)]: a composition of two relations
    >>> compose([(1,2), (2,1), (2,2)], [(1,2), (2,1)])
    [(2, 1), (1, 2), (2, 2)]
    """
    return [y for x in combine(lst_fst, lst_snd) for y in cartesian(x[0], x[1])]
