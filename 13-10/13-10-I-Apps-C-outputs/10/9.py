
def get_ballots_to_cast(k, v, probabilities, ballots):
    # Initialize a list to store the expected number of positions for Yraglac
    expected_positions = []
    
    # Iterate over all possible number of ballots cast by you
    for i in range(2**k):
        # Initialize a list to store the number of ballots cast by each voter
        voter_ballots = [0] * v
        
        # Set the number of ballots cast by you
        voter_ballots[v-1] = i
        
        # Iterate over all voters
        for j in range(v-1):
            # Check if the voter j casts ballots
            if probabilities[j] > 0:
                # Add the number of ballots cast by the voter j to the total number of ballots cast
                voter_ballots[j] = ballots[j]
        
        # Calculate the expected number of positions for Yraglac
        expected_positions.append(calc_expected_positions(k, voter_ballots))
    
    # Return the number of ballots that maximizes the expected number of positions for Yraglac
    return expected_positions.index(max(expected_positions))

def calc_expected_positions(k, ballots):
    # Initialize the expected number of positions for Yraglac to 0
    expected_positions = 0
    
    # Iterate over all positions
    for i in range(k):
        # Calculate the binary representation of the total number of ballots
        binary_repr = bin(sum(ballots))[2:]
        
        # Check if the ith least significant bit is 0
        if binary_repr[-(i+1)] == '0':
            # Increment the expected number of positions for Yraglac
            expected_positions += 1
    
    # Return the expected number of positions for Yraglac
    return expected_positions

if __name__ == '__main__':
    k, v = map(int, input().split())
    probabilities = []
    ballots = []
    
    for i in range(v-1):
        probability, ballot = map(int, input().split())
        probabilities.append(probability)
        ballots.append(ballot)
    
    print(get_ballots_to_cast(k, v, probabilities, ballots))

