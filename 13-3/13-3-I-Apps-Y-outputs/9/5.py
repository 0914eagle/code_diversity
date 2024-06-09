
def f1(n, edges):
    # Your code here
    return res, a, b, c

def f2(...):
    # Your code here
    return ...

if __name__ == '__main__':
    n = int(input())
    edges = []
    for i in range(n - 1):
        edges.append(tuple(map(int, input().split())))
    res, a, b, c = f1(n, edges)
    print(res)
    print(a, b, c)

