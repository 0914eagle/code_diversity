
def get_input():
    return list(map(int, input().split()))

def solve(coins, x):
    return "Yes" if sum(coins) >= x else "No"

def main():
    k, x = get_input()
    coins = [500] * k
    print(solve(coins, x))

if __name__ == '__main__':
    main()

