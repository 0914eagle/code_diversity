
def f1(N, M, C, B, A):
    return sum(1 for i in range(N) if A[i] @ B + C > 0)

def f2(N, M, C, B, A):
    return len([i for i in range(N) if A[i] @ B + C > 0])

if __name__ == '__main__':
    N, M, C = map(int, input().split())
    B = list(map(int, input().split()))
    A = [list(map(int, input().split())) for _ in range(N)]
    print(f1(N, M, C, B, A))
    print(f2(N, M, C, B, A))

