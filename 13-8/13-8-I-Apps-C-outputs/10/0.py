
import math

def get_expected_profit(x, p):
    # Calculate the probability of winning and losing for each bet
    winning_prob = p / 100
    losing_prob = 1 - winning_prob

    # Calculate the expected value of each bet
    expected_value = 2 * winning_prob - 1

    # Calculate the maximum expected profit
    max_expected_profit = x / 100 * sum(expected_value for i in range(100))

    return max_expected_profit

def main():
    x, p = map(float, input().split())
    print(f"{get_expected_profit(x, p):.3f}")

if __name__ == '__main__':
    main()

