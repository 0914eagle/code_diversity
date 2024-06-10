
def get_input():
    n, m = map(int, input().split())
    roads = []
    for _ in range(m):
        a, b, d = map(int, input().split())
        roads.append((a, b, d))
    return n, m, roads

def find_shortest_path(n, m, roads):
    # Initialize the distance of each intersection from Delft as infinity
    dist = [float('inf')] * (n + 1)
    dist[0] = 0

    # Initialize the previous intersection of each intersection as -1
    prev = [-1] * (n + 1)

    # Loop through each intersection
    for _ in range(n - 1):
        # Loop through each road
        for a, b, d in roads:
            # If the distance of the current intersection is less than the distance of the next intersection
            if dist[a] < dist[b]:
                # Update the distance and previous intersection of the next intersection
                dist[b] = dist[a] + d
                prev[b] = a

    # If the distance of Amsterdam is infinity, return "impossible"
    if dist[1] == float('inf'):
        return "impossible"

    # Initialize the path as empty
    path = []

    # Start from Amsterdam
    curr = 1

    # Loop until the previous intersection of the current intersection is 0
    while prev[curr] != 0:
        # Add the current intersection to the path
        path.append(curr)
        # Update the current intersection to the previous intersection
        curr = prev[curr]

    # Add the starting intersection (Delft) to the path
    path.append(0)

    # Return the path in reverse order
    return len(path), path[::-1]

def main():
    n, m, roads = get_input()
    print(*find_shortest_path(n, m, roads))

if __name__ == '__main__':
    main()

