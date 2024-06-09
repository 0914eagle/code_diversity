
import sys
input = sys.stdin.read()

def f1(x, y):
    return x + y

def f2(x, y):
    return x * y

if __name__ == '__main__':
    N = int(input())
    points = []
    for i in range(N):
        x, y = map(int, input().split())
        points.append((x, y))
    # your code here
    print(f1(1, 2))
    print(f2(3, 4))

