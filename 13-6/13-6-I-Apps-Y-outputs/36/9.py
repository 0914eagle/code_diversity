
def get_coins():
    return list(map(int, input().split()))

def solve(coins, x):
    return "Yes" if sum(coins) >= x else "No"

if __name__ == '__main__':
    coins, x = get_coins()
    print(solve(coins, x))

