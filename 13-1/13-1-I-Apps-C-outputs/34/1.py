
def solve():
    N = int(input())
    piles = []
    for i in range(N):
        A, K = map(int, input().split())
        piles.append((A, K))

    while True:
        takahashi_move = True
        for i in range(N):
            A, K = piles[i]
            if A > 0:
                takahashi_move = False
                if A > K:
                    piles[i] = (A - K, K)
                else:
                    piles[i] = (0, K)

        if takahashi_move:
            break

    for A, K in piles:
        if A > 0:
            return "Aoki"

    return "Takahashi"

