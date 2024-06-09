
def solve(N, K, table):
    # Initialize the minimum sum to a large value
    min_sum = 1000000
    # Loop through all possible combinations of domino placements
    for i in range(1 << K):
        # Initialize the sum of visible fields to 0
        sum = 0
        # Loop through each row of the table
        for j in range(N):
            # Initialize the number of dominoes placed in the current row to 0
            num_dominoes = 0
            # Loop through each column of the table
            for k in range(N):
                # Check if a domino is placed in the current column
                if i & (1 << (j * N + k)):
                    # Increment the number of dominoes placed in the current row
                    num_dominoes += 1
                    # Add the value of the current field to the sum of visible fields
                    sum += table[j][k]
            # Check if the number of dominoes placed in the current row is odd
            if num_dominoes % 2 == 1:
                # Subtract the value of the current field from the sum of visible fields
                sum -= table[j][-1]
        # Check if the current combination of domino placements has the minimum sum
        if sum < min_sum:
            # Update the minimum sum
            min_sum = sum
    # Return the minimum sum
    return min_sum

