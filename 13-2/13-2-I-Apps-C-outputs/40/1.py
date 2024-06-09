
def f1(N, v, p):
    # Initialize the expected payout
    expected_payout = 0
    
    # Loop through each hole
    for i in range(1, N * (N + 1) // 2 + 1):
        # Calculate the probability of falling into the hole
        probability = 1
        
        # Loop through each bounce
        for j in range(N):
            # Calculate the probability of bouncing to the top-left, top-right, bottom-left, or bottom-right neighbors
            probability_top_left = p[i - 1][0] if i > 1 else 0
            probability_top_right = p[i - 1][1] if i < N * (N + 1) // 2 else 0
            probability_bottom_left = p[i - 1][2] if i > N else 0
            probability_bottom_right = p[i - 1][3] if i < N * (N + 1) // 2 else 0
            
            # Calculate the probability of falling into the hole
            probability_fall = p[i - 1][4]
            
            # Calculate the total probability of bouncing or falling into the hole
            total_probability = probability_top_left + probability_top_right + probability_bottom_left + probability_bottom_right + probability_fall
            
            # Calculate the new probability of falling into the hole
            probability = probability * (1 - total_probability)
        
        # Add the expected payout for the current hole
        expected_payout += v[i - 1] * probability
    
    # Return the expected payout
    return expected_payout

