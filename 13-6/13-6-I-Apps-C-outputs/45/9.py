
def find_triple_correlation(sequence):
    # Initialize variables
    p = len(sequence)
    a = b = c = n = m = 0

    # Iterate through the sequence
    for i in range(p):
        # Check if the current digit is equal to a
        if sequence[i] == a:
            # Check if the next digit is equal to b
            if i + n < p and sequence[i + n] == b:
                # Check if the digit after b is equal to c
                if i + n + m < p and sequence[i + n + m] == c:
                    # If all conditions are met, return the triple correlation
                    return f"triple correlation {a}({n}){b}({m}){c} found"

    # If no triple correlation is found, return "random sequence"
    return "random sequence"

