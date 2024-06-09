
def f1(N, M):
    # f1(N, M) returns the number of distinct routes that can be set on a single line
    return N * (N - 1) * (N - 2) * ... * (N - M + 1)

def f2(N, M):
    # f2(N, M) returns the last nine digits of the number of distinct routes that can be set
    return str(f1(N, M))[-9:]

if __name__ == '__main__':
    N, M = map(int, input().split())
    print(f2(N, M))

