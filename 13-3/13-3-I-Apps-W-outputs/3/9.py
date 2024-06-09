
def f1(n, x, edges):
    # Calculate the beauty of each vertex
    beauty = [0] * (n + 1)
    for i in range(1, n + 1):
        beauty[i] = x[i - 1]
    
    # Calculate the beauty of each path
    paths = []
    for edge in edges:
        paths.append((edge[0], edge[1], gcd(beauty[edge[0] - 1], beauty[edge[1] - 1])))
    
    # Calculate the sum of the beauties of all paths
    sum_beauty = 0
    for path in paths:
        sum_beauty += path[2]
    
    return sum_beauty % 1000000007

def f2(...):
    # Your code here
    pass

if __name__ == '__main__':
    n = int(input())
    x = list(map(int, input().split()))
    edges = []
    for i in range(n - 1):
        edges.append(list(map(int, input().split())))
    print(f1(n, x, edges))

