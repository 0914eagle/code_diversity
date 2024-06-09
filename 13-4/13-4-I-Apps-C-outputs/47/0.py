
import math

def get_maximum_expected_profit(x, p):
    # Calculate the probability of losing and winning for each bet
    prob_loss = 1 - p
    prob_win = p

    # Calculate the expected value of each bet
    expected_value_loss = -1
    expected_value_win = 2

    # Calculate the maximum expected profit
    max_expected_profit = math.inf
    for i in range(100):
        current_profit = i * expected_value_win * prob_win + (100 - i) * expected_value_loss * prob_loss
        if current_profit < max_expected_profit:
            max_expected_profit = current_profit

    # Calculate the refund amount
    refund_amount = x / 100

    # Calculate the maximum expected profit with refund
    max_expected_profit_with_refund = max_expected_profit + refund_amount

    return max_expected_profit_with_refund

x = 20
p = 49.9
print(get_maximum_expected_profit(x, p))

