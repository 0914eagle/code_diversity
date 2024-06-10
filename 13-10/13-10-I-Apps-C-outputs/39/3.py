
def solve(P, N1, N5, N10, N25):
    coins = [N1, N5, N10, N25]
    max_coins = 0
    for i in range(len(coins)):
        if P % coins[i] == 0 and P // coins[i] <= coins[i]:
            max_coins = max(max_coins, P // coins[i])
    if max_coins == 0:
        return "Impossible"
    else:
        return max_coins

def main():
    P = int(input())
    N1, N5, N10, N25 = map(int, input().split())
    print(solve(P, N1, N5, N10, N25))

if __name__ == '__main__':
    main()

