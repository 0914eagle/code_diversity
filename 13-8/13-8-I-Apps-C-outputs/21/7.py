
def get_path_lengths(n, k_list):
    # Initialize a dictionary to store the path lengths from each fragment to the assembly node
    path_lengths = {}
    
    # Loop through each fragment
    for i in range(n):
        # Initialize the current node as the factorial of the fragment's index
        current_node = k_list[i]!
        # Initialize the path length from the current fragment to the assembly node as 0
        path_length = 0
        
        # Loop until the current node is the assembly node
        while current_node != 1:
            # Get the lowest prime divisor of the current node
            prime_divisor = get_lowest_prime_divisor(current_node)
            # Update the current node to be the quotient of the current node and the lowest prime divisor
            current_node = current_node // prime_divisor
            # Increment the path length by 1
            path_length += 1
        
        # Add the path length from the current fragment to the assembly node to the dictionary
        path_lengths[i] = path_length
    
    return path_lengths

def get_lowest_prime_divisor(n):
    # Initialize a list to store the prime factors of n
    prime_factors = []
    
    # Loop until the square root of n
    for i in range(2, int(n**0.5) + 1):
        # If n is divisible by i, add i to the list of prime factors
        if n % i == 0:
            prime_factors.append(i)
    
    # Return the smallest prime factor
    return min(prime_factors)

def main():
    n = int(input())
    k_list = list(map(int, input().split()))
    path_lengths = get_path_lengths(n, k_list)
    print(sum(path_lengths.values()))

if __name__ == '__main__':
    main()

