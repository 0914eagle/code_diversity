
def solve(N, K, table):
    # Initialize the minimum sum to a large value
    min_sum = 1000000
    # Loop through all possible combinations of dominoes
    for i in range(1 << K):
        # Convert the binary representation of i to a list of indices
        indices = [j for j in range(K) if i & (1 << j)]
        # Initialize the sum of visible fields to 0
        sum_visible = 0
        # Loop through the table and calculate the sum of visible fields
        for row in range(N):
            for col in range(N):
                # Check if the current field is covered by a domino
                covered = any(indices[j] // N == row or indices[j] % N == col for j in range(K))
                # If the field is not covered, add its value to the sum
                if not covered:
                    sum_visible += table[row][col]
        # If the sum of visible fields is smaller than the minimum sum, update the minimum sum
        if sum_visible < min_sum:
            min_sum = sum_visible
    # Return the minimum sum
    return min_sum

