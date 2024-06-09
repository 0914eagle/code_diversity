
import sys
input = sys.stdin.read()

def get_input():
    n, m = map(int, input.split('\n')[0].split())
    roads = []
    for i in range(1, m+1):
        a, b, w = map(int, input.split('\n')[i].split())
        roads.append((a, b, w))
    q = int(input.split('\n')[m+1])
    days = []
    for i in range(m+2, m+2+q):
        s, t = map(int, input.split('\n')[i].split())
        days.append((s, t))
    return n, m, roads, q, days

def f1(n, m, roads, q, days):
    # Write your code here
    return

def f2(n, m, roads, q, days):
    # Write your code here
    return

if __name__ == '__main__':
    n, m, roads, q, days = get_input()
    print(f1(n, m, roads, q, days))
    print(f2(n, m, roads, q, days))

