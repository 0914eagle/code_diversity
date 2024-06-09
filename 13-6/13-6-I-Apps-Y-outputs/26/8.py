
def get_tree_cost(n, a, edges):
    # Initialize the distance array with 0s
    dist = [0] * (n + 1)
    
    # Loop through each edge and update the distance array
    for edge in edges:
        u, v = edge[0], edge[1]
        dist[u] += 1
        dist[v] += 1
    
    # Calculate the cost of the tree
    cost = 0
    for i in range(1, n + 1):
        cost += dist[i] * a[i - 1]
    
    return cost

def main():
    n = int(input())
    a = list(map(int, input().split()))
    edges = []
    for i in range(n - 1):
        edges.append(list(map(int, input().split())))
    print(get_tree_cost(n, a, edges))

if __name__ == '__main__':
    main()

