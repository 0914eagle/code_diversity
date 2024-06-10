
import math

def get_max_expected_profit(x, p):
    # Calculate the expected value of each bet
    expected_value = 2 * p - 1
    
    # Calculate the maximum number of bets that can be made before reaching the refund threshold
    max_bets = math.floor(x / (100 - x) * 100)
    
    # Calculate the maximum expected profit
    max_expected_profit = max_bets * expected_value
    
    return max_expected_profit

def main():
    x = float(input("Enter the refund percentage: "))
    p = float(input("Enter the winning probability: "))
    max_expected_profit = get_max_expected_profit(x, p)
    print(f"The maximum expected profit is: {max_expected_profit:.3f}")

if __name__ == '__main__':
    main()

