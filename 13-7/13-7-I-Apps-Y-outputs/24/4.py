
def get_coins_values(n):
    return list(map(int, input().split()))

def get_queries():
    return list(map(int, input().split()))

def get_min_coins(coins, queries):
    min_coins = []
    for query in queries:
        min_coins.append(get_min_coins_helper(coins, query))
    return min_coins

def get_min_coins_helper(coins, query):
    min_coins = -1
    for i in range(len(coins)):
        if query >= coins[i]:
            if min_coins == -1 or min_coins > 1 + get_min_coins_helper(coins, query - coins[i]):
                min_coins = 1 + get_min_coins_helper(coins, query - coins[i])
    return min_coins

if __name__ == '__main__':
    n = int(input())
    coins = get_coins_values(n)
    q = int(input())
    queries = get_queries()
    min_coins = get_min_coins(coins, queries)
    for min_coin in min_coins:
        print(min_coin)

