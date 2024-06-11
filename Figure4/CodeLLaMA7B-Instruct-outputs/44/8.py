


def change_base(x: int, base: int):
    
    # Check if the base is valid
    if base < 2 or base > 9:
        raise ValueError("Base must be between 2 and 9")

    # Create a list to store the digits of the number in the new base
    new_digits = []

    # Divide the input number by the base and get the remainder
    remainder = x % base

    # Add the remainder to the list of digits
    new_digits.append(str(remainder))

    # Get the quotient of the input number and the base
    quotient = x // base

    # While the quotient is not zero, divide it by the base and get the remainder
    while quotient != 0:
        remainder = quotient % base
        new_digits.append(str(remainder))
        quotient = quotient // base

    # Return the digits in the new base in reverse order
    return ''.join(new_digits[::-1])


