
def can_buy_toy(coins, cost):
    return sum(coins) >= cost

def main():
    coins = list(map(int, input().split()))
    cost = int(input())
    print("Yes") if can_buy_toy(coins, cost) else print("No")

if __name__ == '__main__':
    main()

