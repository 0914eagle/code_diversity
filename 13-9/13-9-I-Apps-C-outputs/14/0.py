
def solve(n, p, coders):
    # Initialize a set to store the two suspects
    suspects = set()
    # Iterate over the coders
    for coder in coders:
        # If the coder agreed with the head's choice, add their names to the suspects set
        if coder[0] in suspects or coder[1] in suspects:
            suspects.add(coder[0])
            suspects.add(coder[1])
    # Return the number of possible two-suspect sets
    return len(suspects)

