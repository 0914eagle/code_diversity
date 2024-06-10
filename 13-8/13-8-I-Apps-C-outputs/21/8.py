
def get_min_distance(fragments, samples):
    # Initialize a dictionary to store the distance of each fragment from the samples
    distances = {}
    for fragment in fragments:
        distances[fragment] = float('inf')
    # Initialize a queue to store the nodes to be processed
    queue = []
    # Add the samples to the queue
    for sample in samples:
        queue.append(sample)
    # Loop until the queue is empty
    while queue:
        # Get the current node from the queue
        node = queue.pop(0)
        # If the node is a fragment, update the distance of the fragment from the samples
        if node in fragments:
            distances[node] = 0
        # If the node is not a fragment, get the neighbors of the node
        else:
            neighbors = get_neighbors(node)
            # Loop through the neighbors
            for neighbor in neighbors:
                # If the neighbor is a fragment, update the distance of the fragment from the samples
                if neighbor in fragments:
                    distances[neighbor] = min(distances[neighbor], distances[node] + 1)
                # If the neighbor is not a fragment, add it to the queue
                else:
                    queue.append(neighbor)
    # Return the minimum distance of all fragments from the samples
    return min(distances.values())

def get_neighbors(node):
    # Get the lowest prime divisor of the node
    f = lowest_prime_divisor(node)
    # Get the neighbors of the node
    neighbors = []
    if f > 1:
        neighbors.append(node // f)
    if node % f == 0:
        neighbors.append(node // f + 1)
    return neighbors

def lowest_prime_divisor(node):
    # Get the prime factors of the node
    factors = prime_factors(node)
    # Get the lowest prime factor
    return min(factors)

def prime_factors(node):
    # Initialize a list to store the prime factors
    factors = []
    # Loop through the numbers from 2 to the square root of the node
    for i in range(2, int(node ** 0.5) + 1):
        # If the node is divisible by the number, add the number to the list of prime factors
        if node % i == 0:
            factors.append(i)
    # If the node is a prime number, add it to the list of prime factors
    if len(factors) == 0:
        factors.append(node)
    return factors

def main():
    # Get the number of fragments and the locations of the fragments
    n = int(input())
    fragments = set(map(int, input().split()))
    # Get the samples
    samples = set(map(int, input().split()))
    # Get the minimum distance of all fragments from the samples
    distance = get_min_distance(fragments, samples)
    # Print the minimum distance
    print(distance)

if __name__ == '__main__':
    main()

