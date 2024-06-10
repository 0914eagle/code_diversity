
import math

def get_max_expected_profit(x, p):
    # Calculate the probability of winning and losing for each bet
    win_prob = p / 100
    lose_prob = 1 - win_prob
    
    # Calculate the expected value of each bet
    win_expected_value = 2
    lose_expected_value = -1
    
    # Calculate the maximum expected profit
    max_expected_profit = 0
    for i in range(1, 101):
        # Calculate the expected value of betting i times
        expected_value = i * win_prob * win_expected_value + (1 - i * win_prob) * lose_expected_value
        
        # Check if the expected value is greater than the maximum expected profit
        if expected_value > max_expected_profit:
            max_expected_profit = expected_value
    
    # Return the maximum expected profit
    return max_expected_profit

def main():
    x = float(input())
    p = float(input())
    print(get_max_expected_profit(x, p))

if __name__ == '__main__':
    main()

