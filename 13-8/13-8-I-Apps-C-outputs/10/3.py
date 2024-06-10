
def get_max_expected_profit(x, p):
    # Calculate the probability of winning and losing
    prob_win = p / 100
    prob_loss = 1 - prob_win
    
    # Calculate the expected value of each bet
    expected_value = prob_win * 2 - prob_loss
    
    # Calculate the maximum expected profit
    max_expected_profit = x / 100 * expected_value
    
    return max_expected_profit

