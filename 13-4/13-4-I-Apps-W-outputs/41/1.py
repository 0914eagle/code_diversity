
def solve(m, n, p):
    # Initialize a dictionary to store the number of sequences for each p value
    num_sequences = {}

    # Iterate over the p values
    for i in range(len(p)):
        # Get the current p value and the corresponding x value
        current_p = p[i]
        current_x = i + 1

        # If the current p value has not been seen before, initialize its count to 1
        if current_p not in num_sequences:
            num_sequences[current_p] = 1

        # If the current p value has been seen before, increment its count
        else:
            num_sequences[current_p] += 1

    # Return the total number of sequences modulo 10^9 + 7
    return sum(num_sequences.values()) % (10**9 + 7)

