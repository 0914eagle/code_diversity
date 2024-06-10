
def get_change(price, coins):
    coins_needed = 0
    coins_available = {1: coins[0], 5: coins[1], 10: coins[2], 25: coins[3]}
    while price > 0 and coins_needed < 4:
        if coins_available[price] > 0:
            coins_needed += 1
            price -= price
        elif price - 5 >= 0 and coins_available[5] > 0:
            coins_needed += 1
            price -= 5
        elif price - 10 >= 0 and coins_available[10] > 0:
            coins_needed += 1
            price -= 10
        elif price - 25 >= 0 and coins_available[25] > 0:
            coins_needed += 1
            price -= 25
        else:
            break
    if price == 0:
        return coins_needed
    else:
        return -1

def main():
    price = int(input())
    coins = [int(x) for x in input().split()]
    result = get_change(price, coins)
    if result == -1:
        print("Impossible")
    else:
        print(result)

if __name__ == '__main__':
    main()

