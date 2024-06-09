
def get_expected_length(n, roads):
    # Initialize a dictionary to store the expected length for each city
    expected_length = {}
    
    # Initialize the expected length for the first city as 0
    expected_length[1] = 0
    
    # Loop through each road
    for u, v in roads:
        # If the expected length for the first city is not already computed
        if u not in expected_length:
            # Compute the expected length for the first city
            expected_length[u] = expected_length[1] + 1
        
        # If the expected length for the second city is not already computed
        if v not in expected_length:
            # Compute the expected length for the second city
            expected_length[v] = expected_length[1] + 1
    
    # Return the expected length for the last city
    return expected_length[n]

def main():
    # Read the number of cities and roads
    n, m = map(int, input().split())
    
    # Read the roads
    roads = []
    for _ in range(m):
        u, v = map(int, input().split())
        roads.append((u, v))
    
    # Call the function to get the expected length
    expected_length = get_expected_length(n, roads)
    
    # Print the expected length
    print(expected_length)

if __name__ == '__main__':
    main()

