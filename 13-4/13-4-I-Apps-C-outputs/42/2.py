
def get_min_path_length(fragments, assembly_node):
    # Initialize a dictionary to store the shortest path length from each fragment to the assembly node
    shortest_path_lengths = {}
    for fragment in fragments:
        shortest_path_lengths[fragment] = float('inf')
    shortest_path_lengths[assembly_node] = 0

    # Loop until a fragment is found with a shortest path length that is not infinite
    while True:
        # Find the fragment with the shortest path length that is not infinite
        current_fragment = None
        for fragment in fragments:
            if shortest_path_lengths[fragment] < float('inf'):
                current_fragment = fragment
                break

        # If no fragment has a shortest path length that is not infinite, then break the loop
        if current_fragment is None:
            break

        # Update the shortest path length for all nodes connected to the current fragment
        for node in get_connected_nodes(current_fragment):
            if node not in fragments:
                continue
            current_path_length = shortest_path_lengths[current_fragment] + 1
            if current_path_length < shortest_path_lengths[node]:
                shortest_path_lengths[node] = current_path_length

    # Return the sum of the shortest path lengths for all fragments
    return sum(shortest_path_lengths.values())

def get_connected_nodes(node):
    # Find the lowest prime divisor of the node
    prime_divisor = get_lowest_prime_divisor(node)

    # Return a list of nodes connected to the current node
    return [node // prime_divisor, node * prime_divisor]

def get_lowest_prime_divisor(node):
    # Find the lowest prime divisor of the node
    for i in range(2, int(node ** 0.5) + 1):
        if node % i == 0:
            return i
    return node

def main():
    # Read the input from stdin
    n = int(input())
    fragments = set(map(int, input().split()))

    # Find the assembly node with the shortest path length
    assembly_node = None
    min_path_length = float('inf')
    for node in fragments:
        path_length = get_min_path_length(fragments, node)
        if path_length < min_path_length:
            min_path_length = path_length
            assembly_node = node

    # Print the sum of the shortest path lengths for all fragments
    print(min_path_length)

if __name__ == '__main__':
    main()

