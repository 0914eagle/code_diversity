
def get_input():
    n = int(input())
    prices = [int(input()) for _ in range(n)]
    return n, prices

def get_discounted_price(prices):
    max_price = max(prices)
    prices.remove(max_price)
    return sum(prices) + max_price // 2

def get_total_price(n, prices):
    if n == 1:
        return prices[0]
    else:
        return get_discounted_price(prices)

def main():
    n, prices = get_input()
    total_price = get_total_price(n, prices)
    print(total_price)

if __name__ == '__main__':
    main()

