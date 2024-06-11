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

    # 1. Check if the value is a string
    # 2. Check if the value is a number
    # 3. Check if the value is equidistant from two integers
    # 4. Return the value

    # 1. Check if the value is a string
    if not isinstance(value, str):
        return 'The value is not a string'

    # 2. Check if the value is a number
    try:
        value = float(value)
    except ValueError:
        return 'The value is not a number'

    # 3. Check if the value is equidistant from two integers
    if value % 1 == 0.5:
        return int(round(value))

    # 4. Return the value
    return int(value)


if