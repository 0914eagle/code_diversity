
import itertools
import math

def get_neighbors(graph, node):
    return graph[node]

def get_path_probability(graph, walk, sentry_probability):
    # Initialize variables
    total_probability = 1
    current_node = walk[0]
    next_node = walk[1]
    previous_node = None

    # Iterate through the walk
    for i in range(1, len(walk)):
        # Calculate the probability of the current node
        probability = (1 - sentry_probability) ** 2

        # If the current node is the same as the previous node, calculate the probability of the sentry being in the current node
        if current_node == previous_node:
            probability += sentry_probability

        # If the current node is not the same as the previous node, calculate the probability of the sentry being in a neighboring node
        else:
            neighbors = get_neighbors(graph, current_node)
            neighbor_probability = 0
            for neighbor in neighbors:
                if neighbor == previous_node:
                    neighbor_probability += sentry_probability
                elif neighbor == next_node:
                    neighbor_probability += (1 - sentry_probability)
            probability += neighbor_probability

        # Update the total probability
        total_probability *= probability

        # Update the current node, next node, and previous node
        previous_node = current_node
        current_node = next_node
        next_node = walk[i + 1]

    # Return the total probability
    return total_probability

def get_sentry_probability(graph, walk):
    # Initialize variables
    sentry_probability = 0
    current_node = walk[0]
    next_node = walk[1]
    previous_node = None

    # Iterate through the walk
    for i in range(1, len(walk)):
        # Calculate the probability of the sentry being in the current node
        probability = 1 / len(get_neighbors(graph, current_node))

        # If the current node is the same as the previous node, calculate the probability of the sentry being in the current node
        if current_node == previous_node:
            sentry_probability += probability

        # If the current node is not the same as the previous node, calculate the probability of the sentry being in a neighboring node
        else:
            neighbors = get_neighbors(graph, current_node)
            neighbor_probability = 0
            for neighbor in neighbors:
                if neighbor == previous_node:
                    neighbor_probability += probability
            sentry_probability += neighbor_probability

        # Update the current node, next node, and previous node
        previous_node = current_node
        current_node = next_node
        next_node = walk[i + 1]

    # Return the sentry probability
    return sentry_probability

def main():
    # Read the input
    num_nodes = int(input())
    num_rooms = int(input())
    walk = [int(i) for i in input().split()]
    graph = {}
    for i in range(num_nodes):
        neighbors = [int(j) for j in input().split()[1:]]
        graph[i] = neighbors

    # Calculate the sentry probability
    sentry_probability = get_sentry_probability(graph, walk)

    # Calculate the path probability
    path_probability = get_path_probability(graph, walk, sentry_probability)

    # Print the result
    print(path_probability)

if __name__ == '__main__':
    main()

