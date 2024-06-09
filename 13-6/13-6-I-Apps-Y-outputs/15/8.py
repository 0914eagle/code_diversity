
def solve():
    N, M = map(int, input().split())
    likes = [set(map(int, input().split())) for _ in range(N)]
    return len(set.intersection(*likes))

