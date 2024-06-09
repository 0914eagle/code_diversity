
def f1(N, M):
    return (N * (N - 1)) // 2 + M

def f2(N, M):
    return N + M

if __name__ == '__main__':
    N, M = map(int, input().split())
    print(f1(N, M))

