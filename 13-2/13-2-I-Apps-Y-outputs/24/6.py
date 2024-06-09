
def get_maximum_weight_subset(n, k, a, edges):
    # Initialize a dictionary to store the weights of the vertices
    weights = {i: a[i - 1] for i in range(1, n + 1)}
    # Initialize a dictionary to store the distances between vertices
    distances = {}
    # Loop through the edges and calculate the distances between vertices
    for edge in edges:
        u, v = edge[0], edge[1]
        distances[(u, v)] = 1
        distances[(v, u)] = 1
    # Loop through the vertices and calculate the maximum weight subset
    max_weight = 0
    for i in range(1, n + 1):
        # Initialize a set to store the vertices in the current subset
        current_subset = set([i])
        # Loop through the vertices again to calculate the weight of the current subset
        current_weight = 0
        for j in range(1, n + 1):
            if j in current_subset:
                continue
            if (i, j) in distances and distances[(i, j)] <= k:
                current_subset.add(j)
                current_weight += weights[j]
        # If the current weight is greater than the maximum weight, update the maximum weight and the maximum weight subset
        if current_weight > max_weight:
            max_weight = current_weight
    return max_weight

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    edges = []
    for i in range(n - 1):
        u, v = map(int, input().split())
        edges.append((u, v))
    print(get_maximum_weight_subset(n, k, a, edges))

if __name__ == '__main__':
    main()

