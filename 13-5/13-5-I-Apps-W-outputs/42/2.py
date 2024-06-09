
def f1(n, m, similar):
    # Initialize the number of ways to split the problems as 0
    ways = 0
    
    # Loop through each pair of similar problems
    for i in range(m):
        # Get the indices of the two similar problems
        u, v = similar[i]
        
        # If problem u is used in division 1 and problem v is used in division 2, or vice versa
        if (u in division_1 and v in division_2) or (v in division_1 and u in division_2):
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
        
        # If problem u is used in division 1 and problem v is used in division 2, or vice versa
        if (u in division_1 and v in division_2) or (v in division_1 and u in division_2):
            # Increment the number of ways to split the problems
            ways += 1
    
    # Return the number of ways to split the problems
    return ways

if __name__ == '__main__':
    n, m = map(int, input().split())
    similar = []
    for _ in range(m):
        similar.append(tuple(map(int, input().split())))
    print(f1(n, m, similar))
    print(f2(n, m, similar))

