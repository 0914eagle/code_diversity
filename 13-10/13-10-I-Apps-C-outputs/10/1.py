
def get_expected_votes(k, b_v, b_i):
    # Calculate the total number of ballots
    total_ballots = b_v + sum(b_i)
    
    # Calculate the expected number of ballots for each position
    expected_ballots = [0] * k
    for i in range(k):
        expected_ballots[i] = total_ballots % 2
        total_ballots //= 2
    
    # Calculate the expected number of positions for Yraglac
    expected_positions = 0
    for i in range(k):
        if expected_ballots[i] == 0:
            expected_positions += 1
    
    return expected_positions

def solve(k, v, p, b):
    # Initialize the maximum expected number of positions for Yraglac
    max_expected_positions = 0
    
    # Initialize the number of ballots to cast
    b_v = 0
    
    # Loop through all possible number of ballots
    for i in range(1, 2**k):
        # Calculate the expected number of positions for Yraglac with the current number of ballots
        expected_positions = get_expected_votes(k, i, b)
        
        # Check if the current number of ballots is a maximum
        if expected_positions > max_expected_positions:
            max_expected_positions = expected_positions
            b_v = i
    
    return b_v

if __name__ == '__main__':
    k, v = map(int, input().split())
    p = [float(input()) for _ in range(v - 1)]
    b = [int(input()) for _ in range(v - 1)]
    print(solve(k, v, p, b))

