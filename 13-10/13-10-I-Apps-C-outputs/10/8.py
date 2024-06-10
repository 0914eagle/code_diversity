
def maximize_yraglac_positions(k, v, p, b):
    # Initialize variables
    total_ballots = 0
    yraglac_positions = 0
    
    # Iterate over each voter
    for i in range(v):
        # Check if voter i votes
        if np.random.rand() < p[i]:
            # Add voter's ballots to total ballots
            total_ballots += b[i]
            
            # Iterate over each position
            for j in range(k):
                # Check if voter i's ballots have a 0 in the jth least significant bit
                if (b[i] >> j) & 1 == 0:
                    # Increment Yraglac's positions
                    yraglac_positions += 1
    
    # Return Yraglac's expected positions
    return yraglac_positions

def solve(k, v, p, b):
    # Initialize variables
    max_yraglac_positions = 0
    max_ballots = 0
    
    # Iterate over each possible number of ballots
    for ballots in range(2**k):
        # Cast ballots and calculate Yraglac's expected positions
        yraglac_positions = maximize_yraglac_positions(k, v, p, ballots)
        
        # Check if Yraglac's expected positions are greater than the current max
        if yraglac_positions > max_yraglac_positions:
            # Update max Yraglac's expected positions and ballots
            max_yraglac_positions = yraglac_positions
            max_ballots = ballots
    
    # Return the number of ballots that maximize Yraglac's expected positions
    return max_ballots

if __name__ == '__main__':
    k, v = map(int, input().split())
    p = []
    b = []
    for i in range(v):
        p_i, b_i = map(int, input().split())
        p.append(p_i)
        b.append(b_i)
    print(solve(k, v, p, b))

