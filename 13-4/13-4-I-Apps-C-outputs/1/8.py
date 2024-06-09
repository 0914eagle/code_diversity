
def f1(N, M):
    # f1 should return the number of distinct routes that can be set
    return N * (N - 1)

def f2(N, M):
    # f2 should return the number of distinct routes that can be set
    return N * (N - 1) * (N - 2)

if __name__ == '__main__':
    N, M = map(int, input().split())
    print(f1(N, M))
    print(f2(N, M))

