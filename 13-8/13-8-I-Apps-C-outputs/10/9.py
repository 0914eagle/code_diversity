
import math

def betting_strategy(x, p):
    
    # Calculate the probability of losing and winning at least once
    losing_prob = 1 - p
    winning_prob = p
    
    # Calculate the expected value of each bet
    expected_value = 2 * p - 1
    
    # Calculate the maximum expected profit
    max_expected_profit = x * expected_value * losing_prob
    
    return max_expected_profit

def main():
    x, p = map(float, input().split())
    print(f"{betting_strategy(x, p):.3f}")

if __name__ == '__main__':
    main()

