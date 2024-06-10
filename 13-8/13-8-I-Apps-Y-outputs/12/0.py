
def get_min_moves(a, k):
    n = len(a)
    x = 0
    moves = 0
    while not all(i % k == 0 for i in a):
        added = False
        for i in range(n):
            if a[i] % k != 0:
                a[i] += x
                added = True
                break
        if added:
            x += 1
            moves += 1
        else:
            x += 1
    return moves

def solve(a, k):
    return get_min_moves(a, k)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        a = list(map(int, input().split()))
        print(solve(a, k))

