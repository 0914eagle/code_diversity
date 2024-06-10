
import math

def expected_profit(x, p):
    # Calculate the probability of winning and losing
    win_prob = p / 100
    lose_prob = 1 - win_prob
    
    # Calculate the expected value of each bet
    win_value = 2
    lose_value = -1
    
    # Calculate the expected value of the entire game
    expected_value = win_prob * win_value + lose_prob * lose_value
    
    # Calculate the maximum expected profit
    max_expected_profit = x / 100 * expected_value
    
    return max_expected_profit

def main():
    x = float(input())
    p = float(input())
    print(expected_profit(x, p))

if __name__ == '__main__':
    main()

