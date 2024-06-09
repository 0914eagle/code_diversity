
def solve(n, p, coders):
    # Initialize a set to store the two suspects
    suspects = set()
    # Iterate over the coders
    for coder in coders:
        # If the coder agrees with the head's choice
        if coder[0] in suspects or coder[1] in suspects:
            # Add the other coder to the set of suspects
            suspects.add(coder[0] if coder[1] in suspects else coder[1])
    # Return the number of possible two-suspect sets
    return len(suspects)

