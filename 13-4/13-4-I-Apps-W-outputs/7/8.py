
def f1(n, m, similar):
    # Initialize the number of ways to split problems as 0
    ways = 0
    
    # Loop through each pair of similar problems
    for i in range(m):
        # Get the indices of the two similar problems
        u, v = similar[i]
        
        # Check if problem u is already used in division 1
        if u in division_1:
            # If problem u is already used in division 1, check if problem v is not used in division 2
            if v not in division_2:
                # If problem v is not used in division 2, add 1 to the number of ways to split problems
                ways += 1
        else:
            # If problem u is not used in division 1, check if problem v is used in division 2
            if v in division_2:
                # If problem v is used in division 2, add 1 to the number of ways to split problems
                ways += 1
    
    # Return the number of ways to split problems
    return ways

def f2(n, m, similar):
    # Initialize the number of ways to split problems as 0
    ways = 0
    
    # Loop through each pair of similar problems
    for i in range(m):
        # Get the indices of the two similar problems
        u, v = similar[i]
        
        # Check if problem u is already used in division 1
        if u in division_1:
            # If problem u is already used in division 1, check if problem v is not used in division 2
            if v not in division_2:
                # If problem v is not used in division 2, add 1 to the number of ways to split problems
                ways += 1
        else:
            # If problem u is not used in division 1, check if problem v is used in division 2
            if v in division_2:
                # If problem v is used in division 2, add 1 to the number of ways to split problems
                ways += 1
    
    # Return the number of ways to split problems
    return ways

if __name__ == '__main__':
    n, m = map(int, input().split())
    similar = []
    for _ in range(m):
        u, v = map(int, input().split())
        similar.append((u, v))
    
    # Initialize the divisions as empty sets
    division_1 = set()
    division_2 = set()
    
    # Call function f1 to count the number of ways to split problems in division 1
    ways_1 = f1(n, m, similar)
    
    # Call function f2 to count the number of ways to split problems in division 2
    ways_2 = f2(n, m, similar)
    
    # Print the total number of ways to split problems
    print(ways_1 + ways_2)

