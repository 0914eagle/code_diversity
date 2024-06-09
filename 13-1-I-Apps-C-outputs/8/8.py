
def solve(N, K, table):
    # Initialize the minimum sum to a large value
    min_sum = 1000000
    # Loop through all possible combinations of dominoes
    for i in range(1 << K):
        # Convert the binary representation of i to a list of domino positions
        dominoes = []
        for j in range(K):
            if i & (1 << j):
                dominoes.append((j, j + 1))
        # Calculate the sum of visible fields for this combination of dominoes
        sum = 0
        for row in range(N):
            for col in range(N):
                # Check if the field is visible (not covered by a domino)
                visible = True
                for domino in dominoes:
                    if (row, col) in domino or (row + 1, col) in domino or (row, col + 1) in domino or (row + 1, col + 1) in domino:
                        visible = False
                        break
                if visible:
                    sum += table[row][col]
        # Update the minimum sum if necessary
        if sum < min_sum:
            min_sum = sum
    # Return the minimum sum
    return min_sum

