
def solve(N, K, table):
    # Initialize the minimum sum to a large value
    min_sum = 1000000
    # Loop through all possible combinations of domino placements
    for i in range(1 << K):
        # Initialize the current sum to 0
        current_sum = 0
        # Loop through each row of the table
        for j in range(N):
            # Initialize the number of dominoes placed in the current row to 0
            num_dominoes = 0
            # Loop through each column of the table
            for k in range(N):
                # Check if a domino is placed in the current position
                if i & (1 << (j * N + k)):
                    # Increment the number of dominoes placed in the current row
                    num_dominoes += 1
                    # Add the value of the current field to the current sum
                    current_sum += table[j][k]
            # If the number of dominoes placed in the current row is odd, subtract the value of the middle field
            if num_dominoes % 2 == 1:
                current_sum -= table[j][(num_dominoes - 1) // 2]
        # If the current sum is less than the minimum sum, update the minimum sum
        if current_sum < min_sum:
            min_sum = current_sum
    # Return the minimum sum
    return min_sum

