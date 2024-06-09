
def get_max_expected_profit(x, p):
    # Calculate the probability of winning and losing for each bet
    win_prob = p / 100
    lose_prob = 1 - win_prob
    
    # Calculate the expected value for each bet
    win_ev = 2
    lose_ev = -1
    
    # Calculate the expected value for the entire game
    expected_value = win_prob * win_ev + lose_prob * lose_ev
    
    # Calculate the maximum expected profit
    max_expected_profit = expected_value - x / 100
    
    return max_expected_profit

