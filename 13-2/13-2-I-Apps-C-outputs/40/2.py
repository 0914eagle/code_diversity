
def f1(N, v, p):
    # Initialize the expected payout
    expected_payout = 0
    
    # Loop through each hole
    for i in range(1, N * (N + 1) // 2 + 1):
        # Calculate the probability of falling into the hole
        probability = p[i - 1][4]
        
        # If the probability is not zero, calculate the expected payout
        if probability != 0:
            # Calculate the expected payout from the hole
            expected_payout_from_hole = v[i - 1] * probability
            
            # Calculate the expected payout from the neighbors
            expected_payout_from_neighbors = 0
            for j in range(i - 1, i + 1):
                if j >= 1 and j <= N * (N + 1) // 2:
                    expected_payout_from_neighbors += p[i - 1][j - 1] * f1(N, v, p)
            
            # Add the expected payout from the hole and neighbors
            expected_payout += expected_payout_from_hole + expected_payout_from_neighbors
    
    # Return the expected payout
    return expected_payout

def f2(N, v, p):
    # Initialize the expected payout
    expected_payout = 0
    
    # Loop through each hole
    for i in range(1, N * (N + 1) // 2 + 1):
        # Calculate the probability of falling into the hole
        probability = p[i - 1][4]
        
        # If the probability is not zero, calculate the expected payout
        if probability != 0:
            # Calculate the expected payout from the hole
            expected_payout_from_hole = v[i - 1] * probability
            
            # Calculate the expected payout from the neighbors
            expected_payout_from_neighbors = 0
            for j in range(i - 1, i + 1):
                if j >= 1 and j <= N * (N + 1) // 2:
                    expected_payout_from_neighbors += p[i - 1][j - 1] * f2(N, v, p)
            
            # Add the expected payout from the hole and neighbors
            expected_payout += expected_payout_from_hole + expected_payout_from_neighbors
    
    # Return the expected payout
    return expected_payout

if __name__ == '__main__':
    # Read the input
    N = int(input())
    v = list(map(int, input().split()))
    p = []
    for i in range(N * (N + 1) // 2):
        p.append(list(map(float, input().split())))
    
    # Calculate the expected payout
    expected_payout = f1(N, v, p)
    
    # Print the expected payout
    print(expected_payout)

