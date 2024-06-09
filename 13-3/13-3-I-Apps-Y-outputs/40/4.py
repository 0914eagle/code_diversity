
def solve(N, A):
    result = []
    for i in range(N):
        max_value = 0
        for j in range(N):
            if j != i and A[j] > max_value:
                max_value = A[j]
        result.append(max_value)
    return result

