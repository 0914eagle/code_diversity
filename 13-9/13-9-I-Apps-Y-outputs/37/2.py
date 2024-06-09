
def solve(a, k):
    n = len(a)
    x = 0
    moves = 0
    while True:
        done = True
        for i in range(n):
            if a[i] % k != 0:
                done = False
                break
        if done:
            return moves
        for i in range(n):
            if a[i] % k != 0:
                a[i] += x
                moves += 1
        x += 1

