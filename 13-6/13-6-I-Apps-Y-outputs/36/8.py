
def get_coins(k):
    return [500] * k

def add_up_to(coins, x):
    return sum(coins) >= x

def solve(k, x):
    coins = get_coins(k)
    return "Yes" if add_up_to(coins, x) else "No"

if __name__ == '__main__':
    k, x = map(int, input().split())
    print(solve(k, x))

