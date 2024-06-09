
def f1(n, x, edges):
    # Calculate the beauty of each vertex
    beauty = [x[i] for i in range(n)]
    for i in range(n - 1):
        u, v = edges[i]
        beauty[v] = gcd(beauty[u], beauty[v])
    
    # Calculate the sum of the beauties of all paths
    sum = 0
    for i in range(n):
        sum += beauty[i]
    
    return sum % 1000000007

def f2(...):
    # Your code here
    pass

if __name__ == '__main__':
    n = int(input())
    x = list(map(int, input().split()))
    edges = []
    for i in range(n - 1):
        u, v = map(int, input().split())
        edges.append((u, v))
    
    print(f1(n, x, edges))

