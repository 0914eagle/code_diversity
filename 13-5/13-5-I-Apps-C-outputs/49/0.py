
def f1(n, m, roads):
    # Your code here
    return

def f2(n, m, roads):
    # Your code here
    return

if __name__ == '__main__':
    n, m = map(int, input().split())
    roads = [tuple(map(int, input().split())) for _ in range(m)]
    print(f1(n, m, roads))
    print(f2(n, m, roads))

