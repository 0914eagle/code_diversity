
def can_start_round_dance(p):
    n = len(p)
    if n == 1:
        return True
    if n == 2:
        return p[0] == 1 and p[1] == 2
    if n == 3:
        return p[0] == 1 and p[1] == 2 and p[2] == 3
    if p[0] != 1:
        return False
    for i in range(1, n):
        if p[i] != i + 1:
            return False
    return True

def solve(q):
    for _ in range(q):
        n = int(input())
        p = list(map(int, input().split()))
        print("YES") if can_start_round_dance(p) else print("NO")

if __name__ == '__main__':
    solve(int(input()))

