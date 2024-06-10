
def get_maximum_bourles(n, m, r, s, b):
    # Initialize variables
    max_bourles = 0
    shares = 0
    total_bourles = r

    # Sort the buy and sell prices
    sorted_buy_prices = sorted(s)
    sorted_sell_prices = sorted(b, reverse=True)

    # Loop through the buy and sell prices
    for i in range(n):
        for j in range(m):
            # Check if the current buy price is less than or equal to the current sell price
            if sorted_buy_prices[i] <= sorted_sell_prices[j]:
                # Buy as many shares as possible at the current buy price
                shares += total_bourles // sorted_buy_prices[i]
                total_bourles %= sorted_buy_prices[i]

                # Sell all shares at the current sell price
                max_bourles += shares * sorted_sell_prices[j]
                shares = 0
                break

    # Return the maximum number of bourles
    return max_bourles

def main():
    n, m, r = map(int, input().split())
    s = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(get_maximum_bourles(n, m, r, s, b))

if __name__ == '__main__':
    main()

