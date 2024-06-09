
import math

def get_maximum_expected_profit(x, p):
    # Calculate the probability of winning and losing for each bet
    win_prob = p / 100
    lose_prob = 1 - win_prob
    
    # Calculate the expected value of each bet
    expected_value = 2 * win_prob - 1
    
    # Calculate the maximum expected profit
    max_expected_profit = x / 100 * expected_value
    
    return round(max_expected_profit, 3)

