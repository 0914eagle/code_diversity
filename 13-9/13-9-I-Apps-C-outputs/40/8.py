
def compute_chances(N, L, walk, graph):
    # Initialize the probability of success as 1
    prob = 1

    # Iterate over the rooms in the walk
    for i in range(L):
        # Get the current room and its neighbors
        current_room = walk[i]
        neighbors = graph[current_room]

        # If the current room has neighbors, calculate the probability of visiting them
        if len(neighbors) > 0:
            # Initialize the probability of visiting a neighbor as 0
            prob_neighbor = 0

            # Iterate over the neighbors
            for neighbor in neighbors:
                # If the neighbor is not the previous room, calculate the probability of visiting it
                if neighbor != walk[i - 1]:
                    prob_neighbor += 1 / len(neighbors)

            # Update the probability of success with the probability of visiting a neighbor
            prob *= prob_neighbor

    # Return the probability of success
    return prob

def main():
    # Read the input
    N, L = map(int, input().split())
    walk = list(map(int, input().split()))
    graph = [[] for _ in range(N)]
    for _ in range(N):
        node, neighbors = map(int, input().split())
        graph[node] = list(map(int, input().split()))

    # Compute the chances of success
    prob = compute_chances(N, L, walk, graph)

    # Print the result
    print(prob)

if __name__ == '__main__':
    main()

