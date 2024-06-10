
def get_coin_values(n):
    return list(map(int, input().split()))

def get_queries(q):
    return list(map(int, input().split()))

def get_min_coins(coin_values, query):
    min_coins = -1
    for coin in coin_values:
        if query >= coin:
            min_coins += 1
            query -= coin
    return min_coins

def main():
    n, q = map(int, input().split())
    coin_values = get_coin_values(n)
    queries = get_queries(q)
    for query in queries:
        print(get_min_coins(coin_values, query))

if __name__ == '__main__':
    main()

