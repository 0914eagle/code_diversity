
def get_maximum_distance(n, k, u, roads):
    # Initialize the distance matrix with 0s
    distance_matrix = [[0 for _ in range(n)] for _ in range(n)]

    # Fill in the distance matrix with the distances between towns
    for road in roads:
        x, y = road
        distance_matrix[x - 1][y - 1] = 1
        distance_matrix[y - 1][x - 1] = 1

    # Use Floyd-Warshall algorithm to find the shortest path between all pairs of towns
    for k in range(n):
        for i in range(n):
            for j in range(n):
                distance_matrix[i][j] = min(distance_matrix[i][j], distance_matrix[i][k] + distance_matrix[k][j])

    # Find the maximum distance by considering all possible pairs of universities
    maximum_distance = 0
    for i in range(k):
        for j in range(i + 1, k):
            maximum_distance = max(maximum_distance, distance_matrix[u[i] - 1][u[j] - 1])

    return maximum_distance

def main():
    n, k = map(int, input().split())
    u = list(map(int, input().split()))
    roads = []
    for _ in range(n - 1):
        x, y = map(int, input().split())
        roads.append((x, y))
    print(get_maximum_distance(n, k, u, roads))

if __name__ == '__main__':
    main()

