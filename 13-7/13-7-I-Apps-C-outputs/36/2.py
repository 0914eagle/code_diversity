
def solve(P, N_1, N_5, N_10, N_25):
    coins = [N_1, N_5, N_10, N_25]
    total = sum(coins)
    if total < P:
        return "Impossible"
    coins_used = [0, 0, 0, 0]
    while P > 0:
        if coins_used[0] < N_1 and P >= 1:
            P -= 1
            coins_used[0] += 1
        elif coins_used[1] < N_5 and P >= 5:
            P -= 5
            coins_used[1] += 1
        elif coins_used[2] < N_10 and P >= 10:
            P -= 10
            coins_used[2] += 1
        elif coins_used[3] < N_25 and P >= 25:
            P -= 25
            coins_used[3] += 1
        else:
            return "Impossible"
    return sum(coins_used)

