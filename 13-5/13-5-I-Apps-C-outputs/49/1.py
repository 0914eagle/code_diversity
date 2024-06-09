
def f1(n, m, roads):
    # Your code here
    return

def f2(n, m, roads):
    # Your code here
    return

if __name__ == '__main__':
    n, m = map(int, input().split())
    roads = []
    for _ in range(m):
        u, v = map(int, input().split())
        roads.append((u, v))
    print(f1(n, m, roads))
    print(f2(n, m, roads))

