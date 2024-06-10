
def get_total_amount(prices):
    # Find the highest price
    highest_price = max(prices)
    # Get the index of the highest price
    highest_price_index = prices.index(highest_price)
    # Calculate the total amount by subtracting the half of the highest price and adding the remaining prices
    total_amount = sum(prices) - highest_price / 2 + prices[highest_price_index]
    return total_amount

def main():
    # Read the number of items and their prices from stdin
    n = int(input())
    prices = [int(x) for x in input().split()]
    # Call the get_total_amount function and print the result
    print(get_total_amount(prices))

if __name__ == '__main__':
    main()

