


def change_base(x: int, base: int):
    
    # Check if the base is valid
    if base < 2 or base >= 10:
        raise ValueError("Base must be between 2 and 9")

    # Create a dictionary to map digits to a new base
    digit_map = {
        0: "0",
        1: "1",
        2: "2",
        3: "3",
        4: "4",
        5: "5",
        6: "6",
        7: "7",
        8: "8",
        9: "9",
    }

    # Create a list to store the digits of the new base
    new_base_digits = []

    # While x is greater than 0
    while x > 0:
        # Get the remainder of x divided by the base
        remainder = x % base
        # Add the digit for the remainder to the list of new base digits
        new_base_digits.append(digit_map[remainder])
        # Divide x by the base to get the next digit
        x //= base

    # Return the new base digits in the correct order
    return "".join(new_base_digits[::-1])


