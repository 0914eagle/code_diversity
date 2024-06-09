
def f1(n, edges):
    # Your code here
    return res, a, b, c

def f2(n, edges):
    # Your code here
    return res, a, b, c

if __name__ == '__main__':
    n = int(input())
    edges = []
    for i in range(n - 1):
        edges.append(tuple(map(int, input().split())))
    res1, a1, b1, c1 = f1(n, edges)
    res2, a2, b2, c2 = f2(n, edges)
    print(res1)
    print(a1, b1, c1)
    print(res2)
    print(a2, b2, c2)

