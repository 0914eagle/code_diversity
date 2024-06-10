
def get_discounted_price(price, discount):
    return price - (price * discount / 100)

def get_total_amount(prices):
    highest_price = max(prices)
    discounted_price = get_discounted_price(highest_price, 50)
    return sum(prices) - discounted_price + highest_price / 2

if __name__ == '__main__':
    num_items = int(input())
    prices = []
    for _ in range(num_items):
        prices.append(int(input()))
    print(get_total_amount(prices))

