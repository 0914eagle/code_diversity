


def change_base(x: int, base: int):
    
    # check if base is valid
    if base < 2 or base >= 10:
        raise ValueError("Base must be between 2 and 9")

    # create a list to store the digits of the number in the new base
    digits = []

    # divide x by the base and get the remainder
    remainder = x % base

    # add the remainder to the list of digits
    digits.append(str(remainder))

    # get the quotient of x / base
    quotient = x // base

    # while the quotient is not 0, repeat the process of dividing by the base and getting the remainder
    while quotient > 0:
        remainder = quotient % base
        digits.append(str(remainder))
        quotient = quotient // base

    # reverse the list of digits and convert it to a string
    return "".join(digits[::-1])


