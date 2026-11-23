"""Fast power.

[Time-Complexity]: O(log |exp|) multiplications for nonzero exp

[Space-Complexity]: O(1) integer variables; integer sizes depend on the result

An algorithm for rapid degree calculation base of exp.

"""


def fast_power(base: int, exp: int, mod: int | None = None) -> int | float:
    """Fast power algorithm.

    Args:
        base: Integer base.
        exp: Integer exponent.
        mod: Optional nonzero integer modulus.

    Raises:
        TypeError: If exp is not an integer.
        ValueError: If mod is zero or a required modular inverse does not exist.
        ZeroDivisionError: If zero is raised to a negative exponent without mod.

    Returns:
        The power, its reciprocal for a negative exponent, or its modular residue.

    """
    if not isinstance(exp, int):
        raise TypeError("exp must be an integer")
    if mod == 0:
        raise ValueError("mod must be nonzero")
    if mod is not None:
        base = pow(base, -1, mod) if exp < 0 else base % mod

    result = 1 if mod is None else 1 % mod
    remaining = abs(exp)
    while remaining:
        if remaining & 1:
            result *= base
            if mod is not None:
                result %= mod
        remaining >>= 1
        if remaining:
            base *= base
            if mod is not None:
                base %= mod

    return 1 / result if exp < 0 and mod is None else result
