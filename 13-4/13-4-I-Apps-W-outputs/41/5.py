
def solve(m, n, p):
    # Initialize a dictionary to store the count of each x sequence
    count = {}

    # Iterate over each p value
    for i in range(len(p)):
        # Get the current p value and the corresponding x value
        curr_p = p[i]
        curr_x = i + 1

        # Check if the x sequence is already in the dictionary
        if curr_x in count:
            # If it is, increment the count for that sequence
            count[curr_x] += 1
        else:
            # If it's not, add it to the dictionary with a count of 1
            count[curr_x] = 1

    # Return the number of unique x sequences
    return len(count)

