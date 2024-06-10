
def get_ballots(k, p, b):
    # Calculate the expected number of ballots for each voter
    expected_ballots = p * b
    
    # Calculate the total number of ballots
    total_ballots = sum(expected_ballots)
    
    # Calculate the expected number of positions for Yraglac
    expected_positions = total_ballots % 2**k
    
    return expected_positions

def get_optimal_ballots(k, v, p, b):
    # Initialize the optimal number of ballots as 0
    optimal_ballots = 0
    
    # Loop through each voter
    for i in range(v):
        # Calculate the expected number of ballots for each voter
        expected_ballots = p[i] * b[i]
        
        # Calculate the total number of ballots
        total_ballots = sum(expected_ballots)
        
        # Calculate the expected number of positions for Yraglac
        expected_positions = total_ballots % 2**k
        
        # If the expected number of positions for Yraglac is greater than the current optimal number of ballots, update the optimal number of ballots
        if expected_positions > optimal_ballots:
            optimal_ballots = expected_positions
    
    return optimal_ballots

if __name__ == '__main__':
    k, v = map(int, input().split())
    p = []
    b = []
    for i in range(v):
        p_i, b_i = map(int, input().split())
        p.append(p_i)
        b.append(b_i)
    print(get_optimal_ballots(k, v, p, b))

