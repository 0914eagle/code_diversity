
def f1(N, H, v, p):
    # Initialize the expected payout
    expected_payout = 0
    
    # Loop through each hole
    for i in range(H):
        # Calculate the probability of falling into the hole
        probability = p[i][4]
        
        # If the probability is not zero, calculate the expected payout
        if probability != 0:
            # Calculate the expected payout from the hole
            expected_payout_from_hole = v[i] * probability
            
            # Calculate the expected payout from the neighbors
            expected_payout_from_neighbors = 0
            for j in range(4):
                if p[i][j] != 0:
                    expected_payout_from_neighbors += p[i][j] * f1(N, H, v, p)
            
            # Add the expected payout from the hole and neighbors
            expected_payout += expected_payout_from_hole + expected_payout_from_neighbors
    
    # Return the expected payout
    return expected_payout

def f2(N, H, v, p):
    # Initialize the expected payout
    expected_payout = 0
    
    # Loop through each hole
    for i in range(H):
        # Calculate the probability of falling into the hole
        probability = p[i][4]
        
        # If the probability is not zero, calculate the expected payout
        if probability != 0:
            # Calculate the expected payout from the hole
            expected_payout_from_hole = v[i] * probability
            
            # Calculate the expected payout from the neighbors
            expected_payout_from_neighbors = 0
            for j in range(4):
                if p[i][j] != 0:
                    expected_payout_from_neighbors += p[i][j] * f2(N, H, v, p)
            
            # Add the expected payout from the hole and neighbors
            expected_payout += expected_payout_from_hole + expected_payout_from_neighbors
    
    # Return the expected payout
    return expected_payout

if __name__ == '__main__':
    N = int(input())
    H = N * (N + 1) // 2
    v = list(map(int, input().split()))
    p = []
    for i in range(H):
        p.append(list(map(float, input().split())))
    
    # Calculate the expected payout using f1 and f2
    expected_payout_f1 = f1(N, H, v, p)
    expected_payout_f2 = f2(N, H, v, p)
    
    # Print the expected payout
    print(expected_payout_f1)
    print(expected_payout_f2)

