
def read_input():
    n, m, s = map(int, input().split())
    people = list(map(int, input().split()))
    roads = []
    for _ in range(m):
        u, v, w = map(int, input().split())
        roads.append((u, v, w))
    shelters = []
    for _ in range(s):
        s, c = map(int, input().split())
        shelters.append((s, c))
    return n, m, s, people, roads, shelters

def optimize_shelters(n, m, s, people, roads, shelters):
    # Initialize the distances from each location to the shelters
    distances = [[float('inf') for _ in range(s)] for _ in range(n)]
    for i in range(s):
        distances[shelters[i][0]][i] = 0

    # Floyd-Warshall algorithm to find the shortest path between all pairs of locations and shelters
    for k in range(n):
        for i in range(n):
            for j in range(s):
                if distances[i][k] + distances[k][j] < distances[i][j]:
                    distances[i][j] = distances[i][k] + distances[k][j]

    # Assign each person to the shelter with the shortest distance
    assigned_shelters = [0] * n
    for i in range(n):
        min_distance = float('inf')
        for j in range(s):
            if distances[i][j] < min_distance:
                min_distance = distances[i][j]
                assigned_shelters[i] = j

    # Calculate the total time it takes to shelter everyone
    total_time = 0
    for i in range(n):
        total_time += min(people[i], shelters[assigned_shelters[i]][1]) * distances[i][assigned_shelters[i]]

    return total_time

def main():
    n, m, s, people, roads, shelters = read_input()
    print(optimize_shelters(n, m, s, people, roads, shelters))

if __name__ == '__main__':
    main()

