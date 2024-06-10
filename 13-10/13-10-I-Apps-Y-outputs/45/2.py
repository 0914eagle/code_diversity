
def get_discount_price(price, discount):
    return price * (1 - discount)

def solve(n, prices):
    highest_price = max(prices)
    highest_price_index = prices.index(highest_price)
    prices[highest_price_index] = get_discount_price(highest_price, 0.5)
    return sum(prices)

if __name__ == '__main__':
    n = int(input())
    prices = list(map(int, input().split()))
    print(solve(n, prices))

