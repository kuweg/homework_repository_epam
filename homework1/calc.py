def check_power_of_2(a: int) -> bool:
    """
    Checking does a given number is a power of 2.
    Bitwise operators wiki:
    https://wiki.python.org/moin/BitwiseOperators
    """
    return not (bool(a & (a - 1)))
