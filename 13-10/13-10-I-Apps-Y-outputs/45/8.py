
def get_discounted_price(prices):
    # Sort the prices in descending order
    prices.sort(reverse=True)
    # Apply the discount of 50% to the highest price
    discounted_price = prices[0] / 2
    # Add the remaining prices to the total
    total = sum(prices[1:]) + discounted_price
    return total

def main():
    # Read the number of items and their prices from stdin
    n = int(input())
    prices = [int(input()) for _ in range(n)]
    # Calculate the total amount Mr. Takaha will pay
    total = get_discounted_price(prices)
    # Print the result
    print(total)

if __name__ == '__main__':
    main()

