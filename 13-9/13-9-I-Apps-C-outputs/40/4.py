
def walk_probability(num_rooms, walk, adjacency_list):
    
    # Initialize the probability of success to 1
    probability = 1

    # Loop through each room in the walk
    for i in range(len(walk)):
        # Get the current room and its neighbors
        current_room = walk[i]
        neighbors = adjacency_list[current_room]

        # Calculate the probability of visiting each neighbor
        visit_probability = 1 / len(neighbors)

        # If the captain is in the last room, he must avoid being captured by the sentry
        if i == len(walk) - 1:
            # Calculate the probability of the sentry being in each neighbor
            sentry_probability = 1 / len(neighbors)

            # Calculate the probability of the sentry being in the current room
            current_room_probability = 1 - sentry_probability

            # Update the probability of success
            probability *= current_room_probability

        # Otherwise, the captain can visit any neighbor with equal probability
        else:
            probability *= visit_probability

    return probability

def main():
    # Read the input
    num_rooms, num_walks, walk = read_input()
    adjacency_list = read_adjacency_list(num_rooms)

    # Calculate the probability of success
    probability = walk_probability(num_rooms, walk, adjacency_list)

    # Print the output
    print(probability)

def read_input():
    
    # Read the number of rooms and the number of walks
    num_rooms, num_walks = map(int, input().split())

    # Read the walk
    walk = list(map(int, input().split()))

    return num_rooms, num_walks, walk

def read_adjacency_list(num_rooms):
    
    # Initialize the adjacency list
    adjacency_list = []

    # Loop through each room
    for i in range(num_rooms):
        # Read the number of neighbors
        num_neighbors = int(input())

        # Read the neighbors
        neighbors = list(map(int, input().split()))

        # Add the neighbors to the adjacency list
        adjacency_list.append(neighbors)

    return adjacency_list

if __name__ == '__main__':
    main()

