
def solve(m, n, p):
    # Initialize a dictionary to store the counts of each x sequence
    counts = {}

    # Iterate over each p value
    for i in range(len(p)):
        # Get the current p value and the corresponding x value
        current_p = p[i]
        current_x = i + 1

        # If the current x value is not already in the dictionary, add it with a count of 1
        if current_x not in counts:
            counts[current_x] = 1
        # Otherwise, increment the count of the current x value
        else:
            counts[current_x] += 1

    # Return the number of unique x sequences that could have generated the p sequence
    return len(counts)

