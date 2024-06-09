
def f1(n, m, similar):
    # Initialize the number of ways to split problems as 0
    ways = 0
    
    # Loop through each pair of similar problems
    for i in range(m):
        # Get the indices of the two similar problems
        u, v = similar[i]
        
        # If problem u is not already used in division 1, increase the number of ways to split problems
        if u not in division_1:
            ways += 1
        
        # If problem v is not already used in division 2, increase the number of ways to split problems
        if v not in division_2:
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
        
        # If problem u is not already used in division 1, increase the number of ways to split problems
        if u not in division_1:
            ways += 1
        
        # If problem v is not already used in division 2, increase the number of ways to split problems
        if v not in division_2:
            ways += 1
    
    # Return the number of ways to split problems
    return ways

if __name__ == '__main__':
    n, m = map(int, input().split())
    similar = []
    for _ in range(m):
        similar.append(list(map(int, input().split())))
    print(f1(n, m, similar))
    print(f2(n, m, similar))

