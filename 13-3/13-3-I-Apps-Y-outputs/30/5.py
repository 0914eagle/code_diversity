
def get_min_chars(route):
    # Initialize variables
    min_chars = 0
    macro_chars = 0
    macro_used = False
    macro = ""

    # Iterate through the route
    for i in range(len(route)):
        # If the current character is not a macro call, increment the minimum number of characters
        if route[i] != "M":
            min_chars += 1
        # If the current character is a macro call, set the macro used flag to True and set the macro to the corresponding string
        else:
            macro_used = True
            macro = route[i+1:]
            break

    # If a macro was used, calculate the number of characters needed for the macro and add it to the minimum number of characters
    if macro_used:
        macro_chars = len(macro)
        min_chars += macro_chars

    return min_chars

