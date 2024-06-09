
def count_ways(n, m, similar):
    # Initialize a list to store the number of ways to split the problems
    ways = [0] * (n + 1)
    ways[0] = 1
    
    # Loop through each pair of similar problems
    for i in range(m):
        # Get the indices of the two similar problems
        u, v = similar[i]
        
        # Loop through each problem from 1 to n
        for k in range(1, n + 1):
            # If the problem is not similar to either of the two similar problems
            if k not in (u, v):
                # Add the number of ways to split the problems without the current problem
                # to the number of ways to split the problems with the current problem
                ways[k] += ways[k - 1]
    
    # Return the number of ways to split the problems
    return ways[n]

def main():
    # Read the number of problems and the number of pairs of similar problems
    n, m = map(int, input().split())
    
    # Read the pairs of similar problems
    similar = []
    for _ in range(m):
        u, v = map(int, input().split())
        similar.append((u, v))
    
    # Call the count_ways function and print the result
    print(count_ways(n, m, similar))

if __name__ == '__main__':
    main()

