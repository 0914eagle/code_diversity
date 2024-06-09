
def solve(N, K, board):
    # Initialize a list to store the sums of the numbers covered by each domino
    sums = []
    
    # Iterate over each possible rotation of the domino
    for i in range(4):
        # Initialize a set to store the fields covered by the domino
        covered_fields = set()
        # Initialize a variable to store the sum of the numbers covered by the domino
        sum = 0
        
        # Iterate over each row of the board
        for j in range(N):
            # If the domino covers this row
            if i % 2 == 0:
                # Add the numbers in the first and third columns to the sum
                sum += board[j][0] + board[j][2]
            else:
                # Add the numbers in the second and third columns to the sum
                sum += board[j][1] + board[j][2]
                
            # Add the indices of the fields covered by the domino to the set
            covered_fields.add((j, 0))
            covered_fields.add((j, 2))
        
        # If the domino covers all fields of the board
        if len(covered_fields) == N * 3:
            # Add the sum to the list of sums
            sums.append(sum)
    
    # Return the maximum sum
    return max(sums)

