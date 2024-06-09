
def f1(n, m, roads):
    # Initialize a dictionary to store the distances between each pair of cities
    distances = {}
    for a, b, w in roads:
        if a not in distances:
            distances[a] = {}
        if b not in distances:
            distances[b] = {}
        distances[a][b] = w
        distances[b][a] = w
    
    # Fill in the distances for each city pair using the bitwise OR operation
    for a in distances:
        for b in distances[a]:
            for c in distances:
                if c != a and c != b:
                    distances[a][c] = distances[a][b] | distances[b][c]
    
    return distances

def f2(distances, queries):
    # Calculate the cost of sending a crystal from city s to city t for each query
    costs = []
    for s, t in queries:
        cost = distances[s][t]
        costs.append(cost)
    
    return costs

if __name__ == '__main__':
    n, m = map(int, input().split())
    roads = []
    for _ in range(m):
        a, b, w = map(int, input().split())
        roads.append((a, b, w))
    q = int(input())
    queries = []
    for _ in range(q):
        s, t = map(int, input().split())
        queries.append((s, t))
    
    distances = f1(n, m, roads)
    costs = f2(distances, queries)
    for cost in costs:
        print(cost)

