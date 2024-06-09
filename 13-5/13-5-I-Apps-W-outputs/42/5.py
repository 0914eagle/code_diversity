
def count_ways_to_split_problems(n, m, similar_problems):
    # Initialize a dictionary to store the number of ways to split problems for each problem
    ways_to_split = {i: 0 for i in range(1, n + 1)}
    
    # Loop through each pair of similar problems
    for u, v in similar_problems:
        # Increment the number of ways to split problems for problem u
        ways_to_split[u] += 1
        # Increment the number of ways to split problems for problem v
        ways_to_split[v] += 1
    
    # Initialize a variable to store the total number of ways to split problems
    total_ways = 0
    
    # Loop through each problem
    for i in range(1, n + 1):
        # If the problem is used in exactly one division
        if ways_to_split[i] == 1:
            # Increment the total number of ways to split problems
            total_ways += 1
    
    # Return the total number of ways to split problems
    return total_ways

def main():
    # Read the number of problems and the number of pairs of similar problems from stdin
    n, m = map(int, input().split())
    
    # Read the pairs of similar problems from stdin
    similar_problems = []
    for _ in range(m):
        u, v = map(int, input().split())
        similar_problems.append((u, v))
    
    # Call the count_ways_to_split_problems function and print the result
    print(count_ways_to_split_problems(n, m, similar_problems))

if __name__ == '__main__':
    main()

