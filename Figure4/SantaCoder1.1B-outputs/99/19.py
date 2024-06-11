def closest_integer(value):
    '''
    Create a function that takes a value (string) representing a number
    and returns the closest integer to it. If the number is equidistant
    from two integers, round it away from zero.

    Examples
    >>> closest_integer("10")
    10
    >>> closest_integer("15.3")
    15

    Note:
    Rounding away from zero means that if the given number is equidistant
    from two integers, the one you should return is the one that is the
    farthest from zero. For example closest_integer("14.5") should
    return 15 and closest_integer("-14.5") should return -15.
    '''
    if '.' in value:
        value = float(value)
    if value == 0:
        return 0
    if value < 0:
        value = -value
    if value < 10:
        return 0
    if value < 100:
        return 1
    if value < 1000:
        return 2
    if value < 10000:
        return 5
    if value < 100000:
        return 10
    if value < 1000000:
        return 20
    if value < 10000000:
        return 50
    if value < 100000000:
        return 100
    if value < 1000000000:
        return 200
    if value < 10000000000:
        return 500
    if value < 100000000000:
        return 1000
    if value < 1000000000000:
        return 2000
    if value < 10000000000000:
        return 5000
    if value < 100000000000000:
        return 10000
    if value < 1000000000000000:
        return 20000
    if value < 10000000000000000:
        return 50000
    if value < 100000000000000000:
        return 100000
    if value < 1000000000000000000:
        return 200000
    if value < 10000000000000000000:
        return 500000
    if value < 100000000000000000000:
        return 10