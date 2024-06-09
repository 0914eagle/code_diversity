
import math

def get_max_expected_profit(x, p):
    # Calculate the probability of winning and losing for each bet
    win_prob = p / 100
    lose_prob = 1 - win_prob
    
    # Calculate the expected value of each bet
    expected_value = win_prob * 2 - lose_prob
    
    # Calculate the maximum expected profit
    max_expected_profit = x / 100 * expected_value
    
    return max_expected_profit

x = 20
p = 49.9
print(get_max_expected_profit(x, p))

