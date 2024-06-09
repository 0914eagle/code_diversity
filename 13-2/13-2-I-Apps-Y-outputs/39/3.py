
def get_max_sum(B):
    
    N = len(B) + 1
    A = [0] * N
    A[0] = B[0]
    for i in range(1, N-1):
        A[i] = max(B[i-1], B[i])
    A[N-1] = B[N-2]
    return sum(A)

