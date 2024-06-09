
def solve(D, q, queries):
    # Initialize a dictionary to store the number of shortest paths between two vertices
    shortest_paths = {}

    # Iterate over each query
    for v, u in queries:
        # If the query is for the same vertex, the number of shortest paths is 1
        if v == u:
            shortest_paths[(v, u)] = 1
            continue

        # Initialize the number of shortest paths to 0
        num_shortest_paths = 0

        # Iterate over all divisors of D
        for d in range(1, D + 1):
            # If d is a divisor of both v and u, and v/d is a prime, increment the number of shortest paths
            if d % v == 0 and d % u == 0 and is_prime(v/d):
                num_shortest_paths += 1

        # Add the number of shortest paths to the dictionary
        shortest_paths[(v, u)] = num_shortest_paths

    # Return the number of shortest paths for each query
    return [shortest_paths[(v, u)] for v, u in queries]

def is_prime(n):
    # Check if n is a prime number
    if n == 1 or n == 0:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def main():
    D, q = map(int, input().split())
    queries = []
    for i in range(q):
        v, u = map(int, input().split())
        queries.append((v, u))
    result = solve(D, q, queries)
    print(*result, sep='\n')

if __name__ == '__main__':
    main()

