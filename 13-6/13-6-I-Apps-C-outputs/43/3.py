
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
            
            # Add the expected payout from the hole to the total expected payout
            expected_payout += expected_payout_from_hole
    
    # Return the total expected payout
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
            
            # Add the expected payout from the hole to the total expected payout
            expected_payout += expected_payout_from_hole
    
    # Return the total expected payout
    return expected_payout

def main():
    # Read the input
    N, H = map(int, input().split())
    v = list(map(int, input().split()))
    p = []
    for _ in range(H):
        p.append(list(map(float, input().split())))
    
    # Calculate the expected payout
    expected_payout = f1(N, H, v, p)
    
    # Print the expected payout
    print(expected_payout)

if __name__ == '__main__':
    main()

