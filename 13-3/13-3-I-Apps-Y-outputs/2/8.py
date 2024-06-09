
def f1(N, M):
    return (N * (N - 1)) // 2

def f2(N, M):
    return (M * (M - 1)) // 2

if __name__ == '__main__':
    N, M = map(int, input().split())
    print(f1(N, M) + f2(N, M))

