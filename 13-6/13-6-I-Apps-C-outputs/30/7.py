
def f1(n, m, roads):
    # Initialize a dictionary to store the distances between each pair of cities
    distances = {}
    for i in range(n):
        distances[i] = {}
        for j in range(n):
            distances[i][j] = 0

    # Fill in the distances between each pair of cities using the given roads
    for road in roads:
        city1, city2, length = road
        distances[city1][city2] = length
        distances[city2][city1] = length

    # Calculate the bitwise OR of all the road lengths for each path between two cities
    for i in range(n):
        for j in range(i+1, n):
            distances[i][j] = distances[i][j] | distances[j][i]

    return distances

def f2(distances, q, queries):
    # Initialize a list to store the transportation costs for each day
    costs = [0] * q

    # Calculate the transportation cost for each day using the given distances and queries
    for i in range(q):
        city1, city2 = queries[i]
        costs[i] = distances[city1][city2]

    return costs

def main():
    n, m = map(int, input().split())
    roads = []
    for i in range(m):
        a, b, w = map(int, input().split())
        roads.append((a, b, w))
    q = int(input())
    queries = []
    for i in range(q):
        s, t = map(int, input().split())
        queries.append((s, t))
    distances = f1(n, m, roads)
    costs = f2(distances, q, queries)
    for cost in costs:
        print(cost)

if __name__ == '__main__':
    main()

