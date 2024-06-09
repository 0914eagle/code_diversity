
def get_min_chars(route):
    # Initialize variables
    num_chars = len(route)
    macro_chars = 0
    macro_used = False

    # Iterate through the route and check for repetition
    for i in range(len(route) - 1):
        if route[i] == route[i + 1]:
            # If a repetition is found, calculate the number of characters needed for the macro
            macro_chars += 2 + len(route[i:i + 2])
            macro_used = True

    # If a macro was used, return the minimum number of characters needed with the macro
    if macro_used:
        return num_chars - macro_chars
    else:
        return num_chars

