
def get_coin_values(n):
    return [int(input()) for _ in range(n)]

def get_queries(q):
    return [int(input()) for _ in range(q)]

def get_min_coins(coin_values, queries):
    min_coins = []
    for query in queries:
        min_coin = -1
        for coin in coin_values:
            if query >= coin:
                min_coin = min(min_coin, query // coin)
        min_coins.append(min_coin)
    return min_coins

def main():
    n, q = map(int, input().split())
    coin_values = get_coin_values(n)
    queries = get_queries(q)
    min_coins = get_min_coins(coin_values, queries)
    for min_coin in min_coins:
        print(min_coin)

if __name__ == '__main__':
    main()

