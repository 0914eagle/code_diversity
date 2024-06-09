
def f1(n, m, similar):
    # Initialize the number of ways to split the problems
    ways = 0
    
    # Iterate over each pair of similar problems
    for i in range(m):
        # Get the indices of the two similar problems
        u, v = similar[i]
        
        # Check if problem u is already used in division 1
        if u in division_1:
            # If problem u is already used in division 1, check if problem v is not used in division 2
            if v not in division_2:
                # If problem v is not used in division 2, increment the number of ways to split the problems
                ways += 1
        else:
            # If problem u is not used in division 1, check if problem v is already used in division 2
            if v in division_2:
                # If problem v is already used in division 2, increment the number of ways to split the problems
                ways += 1
    
    return ways

def f2(n, m, similar):
    # Initialize the number of ways to split the problems
    ways = 0
    
    # Iterate over each pair of similar problems
    for i in range(m):
        # Get the indices of the two similar problems
        u, v = similar[i]
        
        # Check if problem u is already used in division 1
        if u in division_1:
            # If problem u is already used in division 1, check if problem v is not used in division 2
            if v not in division_2:
                # If problem v is not used in division 2, increment the number of ways to split the problems
                ways += 1
        else:
            # If problem u is not used in division 1, check if problem v is already used in division 2
            if v in division_2:
                # If problem v is already used in division 2, increment the number of ways to split the problems
                ways += 1
    
    return ways

if __name__ == '__main__':
    n, m = map(int, input().split())
    similar = []
    for i in range(m):
        u, v = map(int, input().split())
        similar.append((u, v))
    
    # Initialize the divisions
    division_1 = set()
    division_2 = set()
    
    # Iterate over each problem
    for i in range(n):
        # Check if problem i is similar to any other problem
        for j in range(m):
            # Get the indices of the two similar problems
            u, v = similar[j]
            
            # Check if problem i is similar to problem u
            if i == u:
                # If problem i is similar to problem u, add problem v to division 1
                division_1.add(v)
            # Check if problem i is similar to problem v
            elif i == v:
                # If problem i is similar to problem v, add problem u to division 1
                division_1.add(u)
    
    # Count the number of ways to split the problems between division 1 and division 2
    ways = f1(n, m, similar)
    
    # Print the number of ways to split the problems
    print(ways)

