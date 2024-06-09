
def get_min_energy(N, M, alpha, roads):
    # Initialize a graph with N nodes and 0 edges
    graph = [[] for _ in range(N)]

    # Add edges to the graph
    for u, v, c in roads:
        graph[u - 1].append((v - 1, c))
        graph[v - 1].append((u - 1, c))

    # Initialize the minimum energy to infinity
    min_energy = float("inf")

    # Iterate over all possible starting points
    for start in range(N):
        # Initialize the current energy to 0
        current_energy = 0

        # Initialize a set to keep track of visited nodes
        visited = set()

        # Initialize a queue to do BFS
        queue = [start]

        # Do BFS until the queue is empty
        while queue:
            # Get the current node from the queue
            node = queue.pop(0)

            # If the node has already been visited, skip it
            if node in visited:
                continue

            # Add the current node to the visited set
            visited.add(node)

            # Add the energy of the current node to the current energy
            current_energy += graph[node][0][1]

            # If the current energy is greater than the minimum energy, break
            if current_energy > min_energy:
                break

            # Add the neighbors of the current node to the queue
            for neighbor, _ in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

        # If the current energy is less than or equal to the minimum energy, update the minimum energy
        if current_energy <= min_energy:
            min_energy = current_energy

    # Return the minimum energy
    return min_energy

def main():
    N, M, alpha = map(int, input().split())
    roads = []
    for _ in range(M):
        u, v, c = map(int, input().split())
        roads.append((u, v, c))
    print(get_min_energy(N, M, alpha, roads))

if __name__ == '__main__':
    main()

