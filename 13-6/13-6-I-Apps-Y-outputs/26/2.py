
def get_maximum_cost(n, a, edges):
    # Initialize the distance array with 0 for the root vertex
    distance = [0] * n
    # Initialize the cost array with the value of the root vertex
    cost = [a[0]] * n

    # Loop through each edge and update the distance and cost arrays
    for edge in edges:
        u, v = edge
        distance[v] = distance[u] + 1
        cost[v] = cost[u] + a[v]

    # Find the maximum cost by traversing the tree from the root vertex
    max_cost = 0
    for i in range(n):
        max_cost = max(max_cost, cost[i])

    return max_cost

def main():
    n = int(input())
    a = list(map(int, input().split()))
    edges = []
    for i in range(n - 1):
        u, v = map(int, input().split())
        edges.append((u, v))
    print(get_maximum_cost(n, a, edges))

if __name__ == '__main__':
    main()

