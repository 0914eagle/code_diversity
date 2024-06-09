
import math

def get_maximum_expected_profit(x, p):
    # Calculate the probability of winning and losing for each bet
    win_prob = p / 100
    lose_prob = 1 - win_prob
    
    # Calculate the expected value of each bet
    expected_value = win_prob * 2 - lose_prob
    
    # Calculate the maximum expected profit
    maximum_expected_profit = x / 100 * expected_value
    
    return round(maximum_expected_profit, 3)

