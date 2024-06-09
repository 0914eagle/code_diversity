
import sys
input = sys.stdin.read()

def f1(N, points):
    # your code here
    return 0

def f2(N, points):
    # your code here
    return 0

if __name__ == '__main__':
    N = int(input.split('\n')[0])
    points = [tuple(map(int, input.split('\n')[i].split())) for i in range(1, N+1)]
    print(f1(N, points))

