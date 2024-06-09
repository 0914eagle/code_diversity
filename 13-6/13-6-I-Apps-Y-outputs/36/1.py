
def get_coins(k):
    return [500] * k

def can_make_x(coins, x):
    return sum(coins) >= x

def main():
    k, x = map(int, input().split())
    coins = get_coins(k)
    if can_make_x(coins, x):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()

