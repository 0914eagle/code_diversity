
def f1(n, m, similar):
    # Initialize the number of ways to split problems as 0
    ways = 0
    
    # Loop through each pair of similar problems
    for i in range(m):
        # Get the two problems in the pair
        u, v = similar[i]
        
        # Check if problem u is already used in division 1
        if u in division_1:
            # If problem u is already used in division 1, check if problem v is also used in division 1
            if v in division_1:
                # If both problems are used in division 1, increment the number of ways to split problems
                ways += 1
            else:
                # If only problem u is used in division 1, check if problem v is used in division 2
                if v in division_2:
                    # If both problems are used in division 2, increment the number of ways to split problems
                    ways += 1
    
    # Return the number of ways to split problems
    return ways

def f2(n, m, similar):
    # Initialize the number of ways to split problems as 0
    ways = 0
    
    # Loop through each pair of similar problems
    for i in range(m):
        # Get the two problems in the pair
        u, v = similar[i]
        
        # Check if problem u is already used in division 2
        if u in division_2:
            # If problem u is already used in division 2, check if problem v is also used in division 2
            if v in division_2:
                # If both problems are used in division 2, increment the number of ways to split problems
                ways += 1
            else:
                # If only problem u is used in division 2, check if problem v is used in division 1
                if v in division_1:
                    # If both problems are used in division 1, increment the number of ways to split problems
                    ways += 1
    
    # Return the number of ways to split problems
    return ways

if __name__ == '__main__':
    n, m = map(int, input().split())
    similar = []
    for i in range(m):
        u, v = map(int, input().split())
        similar.append((u, v))
    
    # Initialize the sets of problems used in division 1 and 2 as empty sets
    division_1 = set()
    division_2 = set()
    
    # Loop through each problem
    for i in range(1, n+1):
        # Check if problem i is similar to any other problem
        for j in range(m):
            # If problem i is similar to problem j, add problem j to the set of problems used in division 1
            if i in similar[j]:
                division_1.add(j)
                break
    
    # Loop through each problem
    for i in range(1, n+1):
        # Check if problem i is similar to any other problem
        for j in range(m):
            # If problem i is similar to problem j, add problem j to the set of problems used in division 2
            if i in similar[j]:
                division_2.add(j)
                break
    
    # Call function f1 to count the number of ways to split problems in division 1
    ways_1 = f1(n, m, similar)
    
    # Call function f2 to count the number of ways to split problems in division 2
    ways_2 = f2(n, m, similar)
    
    # Print the total number of ways to split problems
    print(ways_1 + ways_2)

