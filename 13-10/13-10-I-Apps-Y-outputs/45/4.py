
def get_total_amount(prices):
    # Sort the prices in descending order
    prices.sort(reverse=True)
    # Apply the discount coupon to the highest price
    discounted_price = prices[0] / 2
    # Calculate the total amount
    total_amount = sum(prices) - discounted_price
    return total_amount

def main():
    # Read the number of items and their prices from stdin
    n = int(input())
    prices = list(map(int, input().split()))
    # Call the get_total_amount function and print the result
    print(get_total_amount(prices))

if __name__ == '__main__':
    main()

