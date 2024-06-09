
def solve():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))

    altars = set()
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if A[i] < B[j] and B[j] < C[k]:
                    altars.add((i, j, k))

    return len(altars)

