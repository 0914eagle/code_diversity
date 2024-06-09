
def get_min_chars(route):
    # Initialize variables
    num_chars = len(route)
    macro_chars = 0
    macro_used = False

    # Iterate through the route and count the number of characters that can be replaced with a macro
    for i in range(len(route) - 1):
        if route[i] == route[i + 1]:
            macro_chars += 1
        else:
            if macro_chars > 0:
                # A macro has been used, so account for the additional characters needed for the macro
                num_chars += 2
                macro_used = True
            macro_chars = 0

    # If a macro was used, account for the additional characters needed for the macro
    if macro_used:
        num_chars += 2

    return num_chars

