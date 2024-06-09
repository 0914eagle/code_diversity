
def solve(N, X, M):
    def euclidean_division(x, m):
        return x % m

    A = [X]
    for i in range(N):
        A.append(euclidean_division(A[i]**2, M))

    return sum(A)

