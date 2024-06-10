
def get_highest_price(prices):
    return max(prices)

def get_discounted_price(highest_price):
    return highest_price / 2

def get_total_amount(prices, discounted_price):
    return sum(prices) - discounted_price + highest_price

def main():
    prices = list(map(int, input().split()))
    highest_price = get_highest_price(prices)
    discounted_price = get_discounted_price(highest_price)
    total_amount = get_total_amount(prices, discounted_price)
    print(total_amount)

if __name__ == '__main__':
    main()

