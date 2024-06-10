
def get_ballots(k, v, p, b):
    # Calculate the expected number of ballots for Yraglac
    expected_ballots = 0
    for i in range(v):
        expected_ballots += p[i] * b[i]
    
    # Calculate the expected number of positions for Yraglac
    expected_positions = 0
    for i in range(k):
        expected_positions += expected_ballots % 2
        expected_ballots //= 2
    
    return expected_positions

def solve(k, v, p, b):
    # Initialize the maximum expected number of positions for Yraglac
    max_expected_positions = 0
    
    # Iterate over all possible number of ballots
    for i in range(2**k):
        # Calculate the expected number of positions for Yraglac for the current number of ballots
        expected_positions = get_ballots(k, v, p, b)
        
        # Update the maximum expected number of positions for Yraglac if necessary
        if expected_positions > max_expected_positions:
            max_expected_positions = expected_positions
    
    return max_expected_positions

if __name__ == '__main__':
    k, v = map(int, input().split())
    p = []
    b = []
    for i in range(v):
        p_i, b_i = map(int, input().split())
        p.append(p_i)
        b.append(b_i)
    print(solve(k, v, p, b))

