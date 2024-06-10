
import math

def get_dist(x1, y1, x2, y2):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

def get_tunnel_length(islands, palm_trees, ratio):
    # Initialize variables
    min_length = 0
    visited = set()
    queue = []

    # Add the first island to the queue
    queue.append(islands[0])
    visited.add(islands[0])

    # Loop through the queue
    while queue:
        # Get the current island
        current_island = queue.pop(0)

        # Check if the current island has a palm tree
        for palm_tree in palm_trees:
            if get_dist(current_island[0], current_island[1], palm_tree[0], palm_tree[1]) <= current_island[2] + palm_tree[2] * ratio:
                # Add the island to the visited set
                visited.add(current_island)

                # Check if all islands have been visited
                if len(visited) == len(islands):
                    return min_length

                # Add the neighboring islands to the queue
                for island in islands:
                    if get_dist(current_island[0], current_island[1], island[0], island[1]) <= current_island[2] + island[2] and island not in visited:
                        queue.append(island)

    # If all islands have not been visited, return impossible
    return "impossible"

def main():
    # Read the input
    n, m, k = map(int, input().split())
    islands = []
    palm_trees = []
    for i in range(n):
        x, y, r = map(int, input().split())
        islands.append((x, y, r))
    for i in range(m):
        x, y, h = map(int, input().split())
        palm_trees.append((x, y, h))

    # Call the function to get the minimum tunnel length
    min_length = get_tunnel_length(islands, palm_trees, k)

    # Print the output
    print(min_length)

if __name__ == '__main__':
    main()

