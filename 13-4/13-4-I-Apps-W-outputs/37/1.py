
def f1(n, edges):
    # Calculate the sum of the weights of all edge-induced subgraphs
    sum_weights = 0
    for i in range(n):
        for j in range(i+1, n):
            sum_weights += 1
    return sum_weights

def f2(n, edges):
    # Calculate the sum of the weights of all edge-induced subgraphs except the null subgraph
    sum_weights = 0
    for i in range(n):
        for j in range(i+1, n):
            if i != j:
                sum_weights += 1
    return sum_weights

if __name__ == '__main__':
    n = int(input())
    edges = []
    for i in range(n-1):
        u, v = map(int, input().split())
        edges.append((u, v))
    print(f2(n, edges) % 998244353)

