
def find_triple_correlation(sequence):
    # Initialize variables
    p = len(sequence)
    a = b = c = 0
    n = m = 0

    # Loop through the sequence and search for triple correlations
    for i in range(p - 2):
        if sequence[i] == a and sequence[i + 1] == b and sequence[i + 2] == c:
            n = i + 1
            m = i + 2
            break

    # If a triple correlation is found, return it
    if n != 0 and m != 0:
        return f"triple correlation {a}({n}){b}({m}){c} found"

    # If no triple correlation is found, return "random sequence"
    else:
        return "random sequence"

