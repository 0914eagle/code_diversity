
import math

def get_max_expected_profit(x, p):
    # Calculate the probability of winning and losing
    win_prob = p / 100
    lose_prob = 1 - win_prob
    
    # Calculate the expected value of each bet
    expect_win = 2
    expect_lose = 1
    
    # Calculate the maximum expected profit
    max_expected_profit = math.inf
    for i in range(1, 1000001):
        expected_profit = i * expect_win * win_prob + (i - x) * expect_lose * lose_prob
        if expected_profit < max_expected_profit:
            break
        max_expected_profit = expected_profit
    
    return max_expected_profit

def main():
    x, p = map(float, input().split())
    print(get_max_expected_profit(x, p))

if __name__ == '__main__':
    main()

