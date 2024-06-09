
import math

def get_maximum_expected_profit(x, p):
    # Calculate the probability of losing and winning for each bet
    prob_lose = 1 - p
    prob_win = p

    # Calculate the expected value of each bet
    expected_value_lose = -1
    expected_value_win = 2

    # Calculate the expected value of the casino refund
    expected_casino_refund = x / 100

    # Calculate the maximum expected profit
    maximum_expected_profit = math.fabs(expected_value_win * prob_win - expected_value_lose * prob_lose + expected_casino_refund)

    return maximum_expected_profit

