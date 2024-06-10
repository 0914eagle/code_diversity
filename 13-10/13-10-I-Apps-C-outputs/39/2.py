
def get_change(price, coins):
    coins = sorted(coins, reverse=True)
    total = 0
    for coin in coins:
        total += coin
        if total == price:
            return coin
        elif total > price:
            return total - price
    return -1

def get_max_coins(price, coins):
    coins = sorted(coins, reverse=True)
    total = 0
    max_coins = 0
    for coin in coins:
        total += coin
        max_coins += 1
        if total == price:
            return max_coins
        elif total > price:
            return max_coins - 1
    return -1

if __name__ == '__main__':
    price = int(input())
    coins = list(map(int, input().split()))
    change = get_change(price, coins)
    if change == -1:
        print("Impossible")
    else:
        print(change)

    max_coins = get_max_coins(price, coins)
    if max_coins == -1:
        print("Impossible")
    else:
        print(max_coins)

