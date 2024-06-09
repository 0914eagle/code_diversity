
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
        # If the character is a macro call, set the macro_used flag to True and update the macro
        elif char == "M":
            macro_used = True
            macro = route[macro_chars:min_chars]
            macro_chars = min_chars + 1
        # If the character is the end of the route, break the loop
        if char == "E":
            break

    # If a macro was used, add the number of characters in the macro to the minimum number of characters
    if macro_used:
        min_chars += len(macro)

    return min_chars

