
def solve(N, K, board):
    # Initialize a list to store the sums of the numbers covered by each domino
    sums = []
    
    # Iterate over each domino
    for i in range(K):
        # Get the current domino
        domino = board[i]
        
        # Calculate the sum of the numbers covered by the domino
        sum = domino[0] + domino[1]
        
        # Add the sum to the list of sums
        sums.append(sum)
    
    # Return the maximum sum
    return max(sums)

