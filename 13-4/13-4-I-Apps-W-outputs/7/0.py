
def f1(n, m, similar):
    # Initialize the number of ways to split the problems as 0
    ways = 0
    
    # Loop through each pair of similar problems
    for i in range(m):
        # Get the indices of the two similar problems
        u, v = similar[i]
        
        # If problem u is not used in any division, we can use it in division 1
        if u not in division1 and u not in division2:
            # Add problem u to division 1
            division1.add(u)
            # Add problem v to division 2
            division2.add(v)
            # Increment the number of ways to split the problems
            ways += 1
    
    # Return the number of ways to split the problems
    return ways

def f2(n, m, similar):
    # Initialize the number of ways to split the problems as 0
    ways = 0
    
    # Loop through each pair of similar problems
    for i in range(m):
        # Get the indices of the two similar problems
        u, v = similar[i]
        
        # If problem v is not used in any division, we can use it in division 2
        if v not in division1 and v not in division2:
            # Add problem u to division 1
            division1.add(u)
            # Add problem v to division 2
            division2.add(v)
            # Increment the number of ways to split the problems
            ways += 1
    
    # Return the number of ways to split the problems
    return ways

def main():
    # Read the input
    n, m = map(int, input().split())
    similar = []
    for _ in range(m):
        u, v = map(int, input().split())
        similar.append((u, v))
    
    # Initialize the divisions as empty sets
    division1 = set()
    division2 = set()
    
    # Call the first function to count the number of ways to split the problems
    ways1 = f1(n, m, similar)
    
    # Call the second function to count the number of ways to split the problems
    ways2 = f2(n, m, similar)
    
    # Print the total number of ways to split the problems
    print(ways1 + ways2)

if __name__ == '__main__':
    main()

