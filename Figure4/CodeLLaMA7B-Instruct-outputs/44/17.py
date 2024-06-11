


def change_base(x: int, base: int):
    
    # check if base is valid
    if base < 2 or base >= 10:
        raise ValueError("Base must be between 2 and 9")

    # create a list to store the digits of the number in the new base
    new_digits = []

    # divide the input number by the base and get the remainder
    remainder = x % base

    # add the remainder to the list of digits
    new_digits.append(str(remainder))

    # divide the input number by the base and get the quotient
    quotient = x // base

    # while the quotient is not 0, keep dividing by the base and getting the remainder
    while quotient != 0:
        remainder = quotient % base
        new_digits.append(str(remainder))
        quotient = quotient // base

    # reverse the list of digits and convert it to a string
    new_digits.reverse()
    return "".join(new_digits)


