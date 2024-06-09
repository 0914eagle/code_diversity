
def read_input():
    N, K, Q = map(int, input().split())
    A = list(map(int, input().split()))
    return N, K, Q, A

def f1(A, K):
    return min(A[:K])

def f2(A, K):
    return max(A[K:]) - min(A[K:])

def solve(N, K, Q, A):
    X, Y = 0, 0
    for i in range(Q):
        smallest = f1(A, K)
        largest = f2(A, K)
        X += largest
        Y += smallest
        A.remove(smallest)
        A = A[1:]
    return X - Y

if __name__ == '__main__':
    N, K, Q, A = read_input()
    print(solve(N, K, Q, A))

