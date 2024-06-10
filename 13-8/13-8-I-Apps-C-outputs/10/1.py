
def get_max_expected_profit(x, p):
    # Calculate the probability of winning and losing a bet
    win_prob = p / 100
    lose_prob = 1 - win_prob
    
    # Calculate the expected value of a single bet
    expected_value = win_prob * 2 - lose_prob
    
    # Calculate the maximum expected profit
    max_expected_profit = x / 100 * expected_value
    
    return max_expected_profit

def main():
    x, p = map(float, input().split())
    max_expected_profit = get_max_expected_profit(x, p)
    print(f"{max_expected_profit:.3f}")

if __name__ == '__main__':
    main()

