
def f1(N, M):
    return M == N

def f2(N, M):
    return "Yes" if M == N else "No"

if __name__ == '__main__':
    N, M = map(int, input().split())
    print(f2(N, M))

