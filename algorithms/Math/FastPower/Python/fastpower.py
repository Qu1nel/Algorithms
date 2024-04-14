"""Fast power.

[Time-Complexity]: O(log2(n))

[Space-Complexity]: O(1)

An algorithm for rapid degree calculation base of exp.

"""


def fast_power(base: int, exp: int) -> int | float:
    """Fast power algorithm.

    Args:
        base: Base of degree.
        exp: Degree.

    Raises:
        AssertionError: if exp is float.

    Returns:
        Result of multiple base in exp.

    """
    assert isinstance(exp, int)

    sign = exp < 0
    exp = abs(exp)

    result = 1
    mult = base

    while exp:
        if exp % 2 == 1:
            result *= mult
        mult *= mult
        exp //= 2

    if sign:
        result = 1 / result

    return result
