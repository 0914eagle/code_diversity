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
    if value == '0':
        return 0
    elif value == '1':
        return 1
    elif value == '2':
        return 2
    elif value == '3':
        return 3
    elif value == '4':
        return 4
    elif value == '5':
        return 5
    elif value == '6':
        return 6
    elif value == '7':
        return 7
    elif value == '8':
        return 8
    elif value == '9':
        return 9
    elif value == '.':
        return 0
    elif value == '-':
        return -1
    elif value == '+':
        return 1
    else:
        return round(float(value))


