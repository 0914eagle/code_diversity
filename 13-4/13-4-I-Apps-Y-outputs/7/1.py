
def f1(N, M, C, B, A):
    return sum(1 for i in range(N) if sum(A[i][j] * B[j] for j in range(M)) + C > 0)

def f2(...):
    ...

if __name__ == '__main__':
    N, M, C = map(int, input().split())
    B = list(map(int, input().split()))
    A = [[int(x) for x in input().split()] for _ in range(N)]
    print(f1(N, M, C, B, A))

