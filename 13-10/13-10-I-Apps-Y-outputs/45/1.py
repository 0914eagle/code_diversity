
def get_discounted_price(prices):
    # find the index of the item with the highest price
    max_index = prices.index(max(prices))
    # apply the discount to the item with the highest price
    prices[max_index] = prices[max_index] // 2
    # return the sum of the prices
    return sum(prices)

def get_total_amount(prices):
    # get the discounted price
    discounted_price = get_discounted_price(prices)
    # print the total amount
    print(f"The total amount is {discounted_price} yen.")

if __name__ == '__main__':
    # get the number of items
    N = int(input())
    # get the prices of the items
    prices = []
    for i in range(N):
        prices.append(int(input()))
    # get the total amount
    get_total_amount(prices)

