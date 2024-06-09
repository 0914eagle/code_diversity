
def solve(m, n, p):
    # Initialize a dictionary to store the counts of each x value
    x_counts = {}

    # Iterate over the p sequence
    for i in range(len(p)):
        # Get the current x value
        x = p[i]

        # If the x value is not in the dictionary, add it with a count of 1
        if x not in x_counts:
            x_counts[x] = 1

        # Otherwise, increment the count of the x value
        else:
            x_counts[x] += 1

    # Initialize a variable to store the total number of sequences
    total_sequences = 1

    # Iterate over the x values and their counts
    for x, count in x_counts.items():
        # Calculate the number of sequences for this x value
        num_sequences = count ** n

        # Multiply the total number of sequences by the number of sequences for this x value
        total_sequences *= num_sequences

        # Take the modulo of the total number of sequences to avoid overflow
        total_sequences %= 1000000007

    # Return the total number of sequences
    return total_sequences

