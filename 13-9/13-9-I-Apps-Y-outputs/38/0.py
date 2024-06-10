
def get_input():
    return map(int, input().split())

def can_buy_toy(coins):
    A, B, C = coins
    return A + B >= C

def main():
    coins = get_input()
    if can_buy_toy(coins):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()

