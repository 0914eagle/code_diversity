
def read_data():
    n, m = map(int, input().split())
    edges = []
    for i in range(n - 1):
        u, v, w = map(int, input().split())
        edges.append((u, v, w))
    queries = list(map(int, input().split()))
    return n, m, edges, queries

def f1(n, m, edges, queries):
    # implement your solution here
    return -1

def f2(n, m, edges, queries):
    # implement your solution here
    return -1

if __name__ == '__main__':
    n, m, edges, queries = read_data()
    print(*f1(n, m, edges, queries), sep='\n')
    print(*f2(n, m, edges, queries), sep='\n')

