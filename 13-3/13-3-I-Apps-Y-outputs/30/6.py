
def get_min_chars(route):
    # Initialize variables
    min_chars = 0
    macro_chars = 0
    macro_used = False
    macro = ""

    # Iterate through the route
    for char in route:
        # If the character is not a macro call, increment the minimum number of characters
        if char not in "MS":
            min_chars += 1
        # If the character is a macro call, set the macro_used flag to True and save the macro
        elif char == "M":
            macro_used = True
            macro = route[macro_chars:min_chars]
            break
        # If the character is a macro character, increment the number of macro characters
        else:
            macro_chars += 1

    # If a macro was used, calculate the number of characters needed for the macro
    if macro_used:
        min_chars += len(macro) - len(set(macro)) + 1

    return min_chars

