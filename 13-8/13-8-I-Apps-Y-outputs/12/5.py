
def get_min_moves(a, k):
    n = len(a)
    x = 0
    moves = 0
    while True:
        flag = False
        for i in range(n):
            if a[i] % k != 0:
                a[i] += x
                flag = True
        if not flag:
            break
        x += 1
        moves += 1
    return moves

def solve(a, k):
    return get_min_moves(a, k)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        a = list(map(int, input().split()))
        print(solve(a, k))

