
# Read input
n, s, t, q = map(int, input().split())
hills = []
for _ in range(n):
    x, y, h = map(int, input().split())
    hills.append((x, y, h))
springs = list(map(int, input().split()))
towns = list(map(int, input().split()))

# Function to calculate distance between two points
def distance(p1, p2):
    return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**0.5

# Function to check if aqueduct can be built between two hills
def can_build_aqueduct(h1, h2, q):
    if abs(h1[2] - h2[2]) > q:
        return False
    return distance(h1, h2) <= q

# Initialize adjacency matrix
adj_matrix = [[float('inf')] * n for _ in range(n)]
for i in range(n):
    adj_matrix[i][i] = 0

# Fill adjacency matrix
for i in range(n):
    for j in range(i+1, n):
        if can_build_aqueduct(hills[i], hills[j], q):
            adj_matrix[i][j] = adj_matrix[j][i] = distance(hills[i], hills[j])

# Floyd-Warshall algorithm to find shortest paths
for k in range(n):
    for i in range(n):
        for j in range(n):
            adj_matrix[i][j] = min(adj_matrix[i][j], adj_matrix[i][k] + adj_matrix[k][j])

# Find the minimum total length of all aqueducts needed
total_length = 0
for town in towns:
    min_length = float('inf')
    for spring in springs:
        min_length = min(min_length, adj_matrix[spring-1][town-1])
    if min_length == float('inf'):
        print("IMPOSSIBLE")
        break
    total_length += min_length

if total_length != float('inf'):
    print("{:.6f}".format(total_length))
