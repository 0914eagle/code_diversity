
def sort_ticket_prices(prices):
    return sorted(prices)

def main():
    prices = list(map(int, input().split()))
    sorted_prices = sort_ticket_prices(prices)
    print(*sorted_prices, sep=' ')

if __name__ == '__main__':
    main()

