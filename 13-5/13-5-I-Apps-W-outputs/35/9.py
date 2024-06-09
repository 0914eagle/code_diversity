
def solve(m, n, p):
    # Initialize a dictionary to store the counts of each x value
    x_counts = {}

    # Iterate through the p sequence and increment the count of each x value
    for x in p:
        if x in x_counts:
            x_counts[x] += 1
        else:
            x_counts[x] = 1

    # Initialize a set to store the unique x values
    unique_x = set()

    # Iterate through the x values and add them to the set if their count is 1
    for x, count in x_counts.items():
        if count == 1:
            unique_x.add(x)

    # Return the number of unique x values modulo 10^9+7
    return len(unique_x) % (10**9+7)

