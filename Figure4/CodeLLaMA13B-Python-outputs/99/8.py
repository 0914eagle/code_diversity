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

    # 1. Check if the value is an integer
    # 2. Check if the value is equidistant from two integers
    # 3. Return the integer that is the farthest from zero

    # 1. Check if the value is an integer
    if value.isdigit():
        return int(value)

    # 2. Check if the value is equidistant from two integers
    # 3. Return the integer that is the farthest from zero
    else:
        # Convert the string to a float
        value = float(value)

        # Get the integer part of the float
        integer = int(value)

        # Get the decimal part of the float
        decimal = value - integer

        # Check if the decimal part is equidistant from two integers
        if decimal == 0.5:
            # Return the integer that is the farthest from zero
            return integer if value > 0 else integer - 1

        # Return the integer that is the closest to the float
        return round(value)


if __name__ == '__main__':
    print(closest_integer("10"))
    print(closest_integer("15.3"))
    print(closest_integer("14.5"))
    print(closest_integer("-14.5"))
