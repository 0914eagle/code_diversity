
def get_min_path_length(n, k_list):
    # Initialize a dictionary to store the distance from each node to the assembly node
    dist = {1: 0}

    # Loop through each fragment
    for i in range(n):
        # Get the current node and the distance from the current node to the assembly node
        curr_node = k_list[i]
        curr_dist = dist[curr_node]

        # Loop through all the prime factors of the current node
        for prime in get_prime_factors(curr_node):
            # If the prime factor is not in the dictionary, add it with the current distance
            if prime not in dist:
                dist[prime] = curr_dist + 1
            # If the prime factor is already in the dictionary, compare the current distance with the stored distance
            # and update the dictionary if the current distance is smaller
            else:
                if curr_dist + 1 < dist[prime]:
                    dist[prime] = curr_dist + 1

    # Return the minimum distance from all the fragments to the assembly node
    return min(dist.values())

def get_prime_factors(n):
    factors = []
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

n = int(input())
k_list = list(map(int, input().split()))
print(get_min_path_length(n, k_list))

