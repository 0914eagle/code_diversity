
import math

def get_maximum_expected_profit(x, p):
    # Calculate the probability of winning and losing for each bet
    win_prob = p / 100
    lose_prob = 1 - win_prob
    
    # Calculate the expected value of each bet
    win_expectation = 2
    lose_expectation = -1
    
    # Calculate the maximum expected profit
    max_expected_profit = 0
    for i in range(1, 11):
        expected_profit = i * win_expectation * win_prob + (10 - i) * lose_expectation * lose_prob
        if expected_profit > max_expected_profit:
            max_expected_profit = expected_profit
    
    # Calculate the refund amount
    refund_amount = x / 100
    
    # Calculate the maximum expected profit with refund
    max_expected_profit_with_refund = max_expected_profit + refund_amount
    
    return max_expected_profit_with_refund

x = 20
p = 49.9
print(get_maximum_expected_profit(x, p))

