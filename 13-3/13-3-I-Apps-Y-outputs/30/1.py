
def get_min_chars(route):
    # Initialize variables
    num_chars = len(route)
    macro_chars = 0
    macro_used = False

    # Iterate through the route and check for repetition
    for i in range(len(route) - 1):
        if route[i] == route[i + 1]:
            # If the current character is repeated, increment the macro character count
            macro_chars += 1
        else:
            # If the current character is not repeated, check if a macro has been used
            if macro_used:
                # If a macro has been used, add the macro character count to the total character count
                num_chars += macro_chars
                # Reset the macro character count
                macro_chars = 0
                # Set the macro used flag to False
                macro_used = False
            # Add the current character to the total character count
            num_chars += 1

    # If a macro has been used, add the macro character count to the total character count
    if macro_used:
        num_chars += macro_chars

    return num_chars

