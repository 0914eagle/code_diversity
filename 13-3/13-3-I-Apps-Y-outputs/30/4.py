
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
        # If the character is a macro call, set the macro_used flag to True and append the character to the macro
        elif char == "M":
            macro_used = True
            macro += char
        # If the character is not a macro call and the macro_used flag is True, increment the number of characters for the macro
        elif macro_used:
            macro_chars += 1
            macro += char

    # If a macro was used, add the number of characters for the macro to the minimum number of characters
    if macro_used:
        min_chars += macro_chars

    return min_chars

