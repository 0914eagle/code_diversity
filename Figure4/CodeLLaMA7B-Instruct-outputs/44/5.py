


def change_base(x: int, base: int):
    
    # Check if the base is valid
    if base < 2 or base >= 10:
        raise ValueError("Base must be between 2 and 9")

    # Create a dictionary to map the digits of the new base
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

    # Create a list to store the digits of the converted number
    converted_digits = []

    # While x is greater than 0, repeat the following steps:
    while x > 0:
        # Take the remainder of x divided by the base, and add it to the list of converted digits
        converted_digits.append(digit_map[x % base])
        # Divide x by the base, and repeat the process until x is 0
        x //= base

    # Return the converted number as a string
    return "".join(converted_digits[::-1])


