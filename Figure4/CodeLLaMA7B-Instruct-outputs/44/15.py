


def change_base(x: int, base: int):
    
    # Check if the base is valid
    if base < 2 or base >= 10:
        raise ValueError("Base must be between 2 and 9")

    # Create a list to store the digits of the number in the new base
    digits = []

    # While x is greater than 0
    while x > 0:
        # Get the remainder when x is divided by the base
        remainder = x % base
        # Add the remainder to the list of digits
        digits.append(str(remainder))
        # Divide x by the base to get the next digit
        x //= base

    # If no digits were added, return 0
    if not digits:
        return "0"

    # Return the digits in the new base as a string
    return "".join(digits[::-1])


