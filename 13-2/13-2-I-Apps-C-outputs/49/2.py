
def f1(n, q, x, y):
    # Your code here
    return ...

def f2(n, q, x, y):
    # Your code here
    return ...

if __name__ == '__main__':
    n, q = map(int, input().split())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    for i in range(q):
        a, b = map(int, input().split())
        print(f1(n, q, x, y, a, b))
        print(f2(n, q, x, y, a, b))

