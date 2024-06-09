
def read_input():
    n, m, s = map(int, input().split())
    people = list(map(int, input().split()))
    roads = []
    for _ in range(m):
        u, v, w = map(int, input().split())
        roads.append((u, v, w))
    shelters = []
    for _ in range(s):
        s_i, c_i = map(int, input().split())
        shelters.append((s_i, c_i))
    return n, m, s, people, roads, shelters

def optimize_shelters(n, m, s, people, roads, shelters):
    # Initialize the distance matrix with infinity
    distance = [[float('inf') for _ in range(n)] for _ in range(n)]
    # Initialize the previous matrix to keep track of the previous node
    previous = [[-1 for _ in range(n)] for _ in range(n)]
    # Initialize the queue with the first node
    queue = [(0, 0)]
    # Loop until the queue is empty
    while queue:
        # Get the current node and its distance
        node, dist = queue.pop(0)
        # If the distance is less than the current distance, update the distance and the previous node
        if distance[node][node] > dist:
            distance[node][node] = dist
            previous[node][node] = node
        # Loop over the neighbors of the current node
        for neighbor, weight in roads:
            # If the distance to the neighbor is less than the current distance, update the distance and the previous node
            if distance[node][neighbor] > dist + weight:
                distance[node][neighbor] = dist + weight
                previous[node][neighbor] = node
                # Add the neighbor to the queue
                queue.append((neighbor, dist + weight))
    # Loop over the shelters
    for s_i, c_i in shelters:
        # Initialize the total weight to 0
        total_weight = 0
        # Initialize the current node to the shelter
        current_node = s_i
        # Loop until the current node is the starting node
        while current_node != 0:
            # Add the weight of the edge to the total weight
            total_weight += distance[current_node][previous[current_node][current_node]]
            # Set the current node to the previous node
            current_node = previous[current_node][current_node]
        # If the total weight is less than the capacity of the shelter, return the shelter
        if total_weight <= c_i:
            return s_i
    # If no shelter is found, return -1
    return -1

def main():
    n, m, s, people, roads, shelters = read_input()
    print(optimize_shelters(n, m, s, people, roads, shelters))

if __name__ == '__main__':
    main()

