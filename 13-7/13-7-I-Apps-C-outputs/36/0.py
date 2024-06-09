
def solve(P, N_1, N_5, N_10, N_25):
    coins = [N_1, N_5, N_10, N_25]
    total = sum(coins)
    if total < P:
        return "Impossible"
    coins.sort(reverse=True)
    count = 0
    for i in range(len(coins)):
        count += coins[i]
        if count >= P:
            return count
    return "Impossible"

