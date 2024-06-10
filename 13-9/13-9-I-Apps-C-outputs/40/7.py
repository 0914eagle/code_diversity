
def calculate_chances(N, L, walk, neighbors):
    # Initialize the probability of success to 1
    probability = 1

    # Iterate over the rooms in the walk
    for i in range(L):
        # Get the current room and its neighbors
        current_room = walk[i]
        current_neighbors = neighbors[current_room]

        # Calculate the probability of succeeding in the current room
        probability *= 1 - (1 / len(current_neighbors))

        # If the sentry is in the current room, multiply the probability by the number of neighbors
        if current_room in current_neighbors:
            probability *= len(current_neighbors)

    # Return the probability of success
    return probability

def main():
    # Read the input
    N, L = map(int, input().split())
    walk = list(map(int, input().split()))
    neighbors = [[] for i in range(N)]
    for i in range(N):
        n, = map(int, input().split())
        for j in range(n):
            neighbors[i].append(int(input()))

    # Calculate the chances of success
    probability = calculate_chances(N, L, walk, neighbors)

    # Print the result
    print(probability)

if __name__ == '__main__':
    main()

