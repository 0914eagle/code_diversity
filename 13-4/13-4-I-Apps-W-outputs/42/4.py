
def solve():
    N = int(input())
    A = list(map(int, input().split()))
    count = 0
    for i in range(N):
        for j in range(N):
            if i != j and A[j] % A[i] == 0:
                break
        else:
            count += 1
    return count

