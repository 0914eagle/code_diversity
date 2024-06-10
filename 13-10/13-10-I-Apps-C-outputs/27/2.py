
def get_max_distance(n, k, u, roads):
    # Initialize the distance matrix with 0s
    dist_matrix = [[0 for _ in range(n)] for _ in range(n)]

    # Fill the distance matrix with the lengths of the roads
    for road in roads:
        dist_matrix[road[0] - 1][road[1] - 1] = 1
        dist_matrix[road[1] - 1][road[0] - 1] = 1

    # Use Floyd-Warshall algorithm to find the shortest path between all pairs of towns
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist_matrix[i][j] = min(dist_matrix[i][j], dist_matrix[i][k] + dist_matrix[k][j])

    # Find the maximum distance by comparing the distances between all pairs of universities
    max_distance = 0
    for i in range(k):
        for j in range(i + 1, k):
            max_distance = max(max_distance, dist_matrix[u[i] - 1][u[j] - 1])

    return max_distance

def main():
    n, k = map(int, input().split())
    u = list(map(int, input().split()))
    roads = []
    for _ in range(n - 1):
        x, y = map(int, input().split())
        roads.append([x, y])
    print(get_max_distance(n, k, u, roads))

if __name__ == '__main__':
    main()

