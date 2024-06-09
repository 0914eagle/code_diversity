
def f1(N, H, v, p):
    # Initialize the expected payout
    expected_payout = 0
    
    # Loop through each hole
    for i in range(H):
        # Calculate the probability of falling into the hole
        probability_fall = 1 - sum(p[i])
        
        # Calculate the expected payout if the ball falls into the hole
        expected_payout_fall = v[i] * probability_fall
        
        # Calculate the expected payout if the ball bounces to a neighbor
        expected_payout_bounce = 0
        for j in range(4):
            if p[i][j] > 0:
                expected_payout_bounce += p[i][j] * f1(N, H, v, p)
        
        # Add the expected payout for this hole to the total expected payout
        expected_payout += expected_payout_fall + expected_payout_bounce
    
    # Return the expected payout
    return expected_payout

def f2(N, H, v, p):
    # Initialize the expected payout
    expected_payout = 0
    
    # Loop through each hole
    for i in range(H):
        # Calculate the probability of falling into the hole
        probability_fall = 1 - sum(p[i])
        
        # Calculate the expected payout if the ball falls into the hole
        expected_payout_fall = v[i] * probability_fall
        
        # Calculate the expected payout if the ball bounces to a neighbor
        expected_payout_bounce = 0
        for j in range(4):
            if p[i][j] > 0:
                expected_payout_bounce += p[i][j] * f2(N, H, v, p)
        
        # Add the expected payout for this hole to the total expected payout
        expected_payout += expected_payout_fall + expected_payout_bounce
    
    # Return the expected payout
    return expected_payout

if __name__ == '__main__':
    N = int(input())
    H = int(input())
    v = list(map(int, input().split()))
    p = []
    for i in range(H):
        p.append(list(map(float, input().split())))
    
    # Calculate the expected payout for the first function
    expected_payout_1 = f1(N, H, v, p)
    
    # Calculate the expected payout for the second function
    expected_payout_2 = f2(N, H, v, p)
    
    # Print the expected payout
    print(expected_payout_1)
    print(expected_payout_2)

