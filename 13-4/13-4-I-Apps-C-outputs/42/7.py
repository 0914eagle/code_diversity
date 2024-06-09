
def get_min_path_length(n, k):
    # Initialize a dictionary to store the shortest path length from each fragment to the assembly node
    shortest_path_length = {}

    # Loop through each fragment
    for i in range(n):
        # Initialize the current node as the fragment's location
        current_node = k[i]

        # Loop until the current node is the assembly node
        while current_node != 1:
            # Get the lowest prime factor of the current node
            prime_factor = get_lowest_prime_factor(current_node)

            # Update the current node to be the node divided by the lowest prime factor
            current_node = current_node // prime_factor

            # If the current node is not in the dictionary, add it with a path length of 1
            if current_node not in shortest_path_length:
                shortest_path_length[current_node] = 1
            # Otherwise, increment the path length by 1
            else:
                shortest_path_length[current_node] += 1

    # Return the sum of the path lengths for all fragments
    return sum(shortest_path_length.values())

def get_lowest_prime_factor(n):
    # Loop through all prime numbers less than or equal to the input number
    for i in range(2, int(n ** 0.5) + 1):
        # If the input number is divisible by the prime number, return the prime number
        if n % i == 0:
            return i

    # If the input number is a prime number, return the input number
    return n

n = int(input())
k = list(map(int, input().split()))
print(get_min_path_length(n, k))

