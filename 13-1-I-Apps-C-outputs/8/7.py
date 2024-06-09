
def solve(N, K, table):
    # Initialize the minimum sum to a large value
    min_sum = 1000000
    # Loop through all possible combinations of dominoes
    for i in range(1 << K):
        # Initialize the current sum to 0
        current_sum = 0
        # Loop through the table
        for j in range(N):
            for k in range(N):
                # Check if the current field is covered by a domino
                if i & (1 << (j * N + k)):
                    # If it is covered, add the value to the current sum
                    current_sum += table[j][k]
        # If the current sum is smaller than the minimum sum, update the minimum sum
        if current_sum < min_sum:
            min_sum = current_sum
    # Return the minimum sum
    return min_sum

