
def get_maximum_expected_profit(x, p):
    # Calculate the expected value of each bet
    expected_value = 2 * p - 1
    
    # Calculate the maximum expected profit
    maximum_expected_profit = x * expected_value
    
    return maximum_expected_profit
    
def main():
    x, p = map(float, input().split())
    print(f"{get_maximum_expected_profit(x, p):.3f}")
    
if __name__ == '__main__':
    main()

