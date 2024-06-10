
import math

def compute_chance(n, l, walk, graph):
    # Initialize the probability of success to 1
    probability = 1

    # Loop through each room in the walk
    for i in range(l):
        # Get the current room and its neighbors
        current_room = walk[i]
        neighbors = graph[current_room]

        # Loop through each neighbor of the current room
        for neighbor in neighbors:
            # If the neighbor is not the previous room, update the probability
            if neighbor != walk[i - 1]:
                probability *= 0.5

    # Return the probability of success
    return probability

def main():
    # Read the input
    n, l = map(int, input().split())
    walk = list(map(int, input().split()))
    graph = [[] for _ in range(n)]
    for _ in range(n):
        n_neighbors, *neighbors = map(int, input().split())
        graph[n_neighbors] = neighbors

    # Compute the chance of success
    chance = compute_chance(n, l, walk, graph)

    # Print the result
    print(chance)

if __name__ == '__main__':
    main()

