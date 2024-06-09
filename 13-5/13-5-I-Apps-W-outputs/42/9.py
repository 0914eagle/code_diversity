
def f1(n, m, similarities):
    # Initialize the number of ways to split problems as 0
    ways = 0
    
    # Loop through each pair of similar problems
    for i in range(m):
        # Get the indices of the two similar problems
        u, v = similarities[i]
        
        # If problem u is not yet used in division 1, increment the number of ways to split problems
        if u not in division_1:
            ways += 1
    
    # Return the number of ways to split problems
    return ways

def f2(n, m, similarities):
    # Initialize the number of ways to split problems as 0
    ways = 0
    
    # Loop through each pair of similar problems
    for i in range(m):
        # Get the indices of the two similar problems
        u, v = similarities[i]
        
        # If problem v is not yet used in division 2, increment the number of ways to split problems
        if v not in division_2:
            ways += 1
    
    # Return the number of ways to split problems
    return ways

def main():
    # Read the input data
    n, m = map(int, input().split())
    similarities = []
    for _ in range(m):
        u, v = map(int, input().split())
        similarities.append((u, v))
    
    # Call the first function to get the number of ways to split problems in division 1
    ways_1 = f1(n, m, similarities)
    
    # Call the second function to get the number of ways to split problems in division 2
    ways_2 = f2(n, m, similarities)
    
    # Print the total number of ways to split problems
    print(ways_1 + ways_2)

if __name__ == '__main__':
    main()

