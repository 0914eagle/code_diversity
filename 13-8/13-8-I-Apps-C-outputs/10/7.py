
def get_maximum_expected_profit(x, p):
    # Calculate the expected value of each bet
    expected_value = 2 - 1 + (x / 100)
    
    # Calculate the maximum expected profit
    maximum_expected_profit = expected_value * p
    
    return maximum_expected_profit

def main():
    x = float(input("Enter the refund percentage: "))
    p = float(input("Enter the winning probability: "))
    maximum_expected_profit = get_maximum_expected_profit(x, p)
    print(f"The maximum expected profit is: {maximum_expected_profit:.3f}")

if __name__ == '__main__':
    main()

