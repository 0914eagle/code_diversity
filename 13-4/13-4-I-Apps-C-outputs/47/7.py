
def get_maximum_expected_profit(x, p):
    # Calculate the probability of winning and losing for each bet
    win_prob = p / 100
    lose_prob = 1 - win_prob

    # Calculate the expected value for each bet
    win_expectation = 2
    lose_expectation = -1

    # Calculate the expected value for the entire game
    expected_value = win_prob * win_expectation + lose_prob * lose_expectation

    # Calculate the maximum expected profit
    maximum_expected_profit = expected_value - x / 100

    return maximum_expected_profit

