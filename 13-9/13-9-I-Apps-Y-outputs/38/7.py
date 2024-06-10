
def get_change(coins, total):
    coins.sort(reverse=True)
    change = []
    for coin in coins:
        while total >= coin:
            total -= coin
            change.append(coin)
    return change

def solve(A, B, C):
    coins = [A, B]
    change = get_change(coins, C)
    if sum(change) == C:
        return "Yes"
    else:
        return "No"

if __name__ == '__main__':
    A, B, C = map(int, input().split())
    print(solve(A, B, C))

