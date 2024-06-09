
import sys
input = sys.stdin.read()

def f1(N, M):
    # your code here
    return N * (N - 1) // 2

def f2(N, M):
    # your code here
    return M

if __name__ == '__main__':
    N, M = map(int, input.split())
    print(f1(N, M))

