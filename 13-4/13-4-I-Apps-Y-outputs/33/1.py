
def solve(N, X, L):
    count = 0
    for i in range(N):
        if L[i] + i <= X:
            count += 1
    return count

