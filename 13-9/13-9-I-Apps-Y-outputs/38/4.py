
def get_input():
    return list(map(int, input().split()))

def can_buy_toy(coins):
    return sum(coins) >= C

def main():
    A, B, C = get_input()
    coins = [A, B]
    print("Yes") if can_buy_toy(coins) else print("No")

if __name__ == '__main__':
    main()

