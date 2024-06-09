
def solve(P, N_1, N_5, N_10, N_25):
    coins = [N_1, N_5, N_10, N_25]
    total = sum(coins)
    if P > total:
        return "Impossible"
    else:
        return max(coins)

