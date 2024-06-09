
def solve(N, M, A):
    total_votes = sum(A)
    A.sort(reverse=True)
    for i in range(M):
        if A[i] < total_votes / (4 * M):
            return "No"
    return "Yes"

