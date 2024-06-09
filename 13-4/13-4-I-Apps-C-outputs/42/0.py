
def get_min_path_length(n, k):
    # Initialize a dictionary to store the shortest path length from each fragment to the assembly node
    shortest_path_length = {}

    # Loop through each fragment
    for i in range(n):
        # Initialize the shortest path length for this fragment to infinity
        shortest_path_length[i] = float('inf')

        # Loop through each node in the system
        for j in range(1, k[i]! + 1):
            # If the current node is the fragment's location, set the shortest path length to 0
            if j == k[i]!:
                shortest_path_length[i] = 0
                break

            # If the current node is not the fragment's location, find the shortest path length from the current node to the fragment's location
            else:
                # Find the lowest prime divisor of the current node
                prime_divisor = get_lowest_prime_divisor(j)

                # If the current node is not a prime number, find the shortest path length from the current node to the fragment's location through the prime divisor
                if prime_divisor != 1:
                    shortest_path_length[i] = min(shortest_path_length[i], shortest_path_length.get(prime_divisor, float('inf')) + 1)

        # If the shortest path length for this fragment is still infinity, set it to 0
        if shortest_path_length[i] == float('inf'):
            shortest_path_length[i] = 0

    # Return the sum of the shortest path lengths for all fragments
    return sum(shortest_path_length.values())

def get_lowest_prime_divisor(n):
    # Initialize the lowest prime divisor as 1
    lowest_prime_divisor = 1

    # Loop through each prime number less than or equal to the square root of the input number
    for i in range(2, int(n**0.5) + 1):
        # If the input number is divisible by the current prime number, set the lowest prime divisor as the current prime number
        if n % i == 0:
            lowest_prime_divisor = i
            break

    # Return the lowest prime divisor
    return lowest_prime_divisor

n = int(input())
k = list(map(int, input().split()))
print(get_min_path_length(n, k))

