
def get_input():
    return list(map(int, input().split()))

def can_buy_toy(coins, cost):
    return sum(coins) >= cost

def main():
    coins = get_input()
    cost = get_input()
    if can_buy_toy(coins, cost):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()

