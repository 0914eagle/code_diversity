
def f1(N, H, p, v):
    # Initialize the expected payout
    expected_payout = 0
    
    # Loop through each hole
    for i in range(H):
        # Calculate the probability of falling into the hole
        probability = p[i][4]
        
        # If the ball falls into the hole, the game ends and the expected payout is the payout of the hole
        if probability == 1:
            expected_payout += v[i]
        
        # If the ball does not fall into the hole, calculate the expected payout for the next round
        else:
            # Calculate the expected payout for each neighbor
            expected_payout_neighbors = [v[j] * p[i][j] for j in range(4)]
            
            # Calculate the expected payout for the next round
            expected_payout_next_round = sum(expected_payout_neighbors)
            
            # Add the expected payout for the next round to the expected payout
            expected_payout += probability * expected_payout_next_round
    
    # Return the expected payout
    return expected_payout

def f2(N, H, p, v):
    # Initialize the expected payout
    expected_payout = 0
    
    # Loop through each hole
    for i in range(H):
        # Calculate the probability of falling into the hole
        probability = p[i][4]
        
        # If the ball falls into the hole, the game ends and the expected payout is the payout of the hole
        if probability == 1:
            expected_payout += v[i]
        
        # If the ball does not fall into the hole, calculate the expected payout for the next round
        else:
            # Calculate the expected payout for each neighbor
            expected_payout_neighbors = [v[j] * p[i][j] for j in range(4)]
            
            # Calculate the expected payout for the next round
            expected_payout_next_round = sum(expected_payout_neighbors)
            
            # Add the expected payout for the next round to the expected payout
            expected_payout += probability * expected_payout_next_round
    
    # Return the expected payout
    return expected_payout

if __name__ == '__main__':
    N = int(input())
    H = N * (N + 1) // 2
    v = list(map(int, input().split()))
    p = []
    for i in range(H):
        p.append(list(map(float, input().split())))
    
    # Calculate the expected payout for the first round
    expected_payout = f1(N, H, p, v)
    
    # Calculate the expected payout for the second round
    expected_payout += f2(N, H, p, v)
    
    # Print the expected payout
    print(expected_payout)

