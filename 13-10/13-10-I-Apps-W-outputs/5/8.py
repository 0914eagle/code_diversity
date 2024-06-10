
def get_distances(n, distances):
    # Convert the list of distances to a matrix
    distance_matrix = []
    for i in range(n):
        distance_matrix.append([0] * n)
    for i in range(n):
        for j in range(n):
            distance_matrix[i][j] = distances[i * n + j]
    return distance_matrix

def get_shortest_distance(distance_matrix, s, t):
    # Floyd-Warshall algorithm
    n = len(distance_matrix)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                distance_matrix[i][j] = min(distance_matrix[i][j], distance_matrix[i][k] + distance_matrix[k][j])
    return distance_matrix[s - 1][t - 1]

def main():
    n, distances, s, t = map(int, input().split())
    distance_matrix = get_distances(n, distances)
    print(get_shortest_distance(distance_matrix, s, t))

if __name__ == '__main__':
    main()

