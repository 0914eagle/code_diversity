
def find_triple_correlation(sequence):
    # Initialize variables
    p = len(sequence)
    a = b = c = n = m = 0

    # Iterate through the sequence
    for i in range(p - 2):
        # Check if the current digit is a
        if sequence[i] == a:
            # Check if the next digit is b
            if sequence[i + 1] == b:
                # Check if the digit after b is c
                if sequence[i + 2] == c:
                    # If all conditions are met, return the triple correlation
                    return f"triple correlation {a}({n}){b}({m}){c} found"

    # If no triple correlation is found, return "random sequence"
    return "random sequence"

