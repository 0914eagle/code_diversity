
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

# Initialize variables
total_length = 0
connections = []

# Calculate minimum total length of aqueducts
for town in towns:
    min_length = float('inf')
    for spring in springs:
        length = distance(hills[town-1], hills[spring-1])
        if length < min_length:
            min_length = length
    if min_length == float('inf'):
        print("IMPOSSIBLE")
        break
    total_length += min_length
else:
    print("{:.6f}".format(total_length))
