
import math

def get_max_expected_profit(x, p):
    # Calculate the probability of losing and winning
    losing_prob = 1 - p
    winning_prob = p

    # Calculate the expected value of each bet
    expected_value = winning_prob * 2 - losing_prob

    # Calculate the maximum expected profit
    max_expected_profit = x / 100 * expected_value

    return max_expected_profit

x = 20
p = 49.9
print(get_max_expected_profit(x, p))

