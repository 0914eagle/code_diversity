
def f1(n, roads):
    # Calculate the number of possible sets of roads that can be flipped
    num_sets = (2**n) - 1
    
    # Initialize a list to store the results
    results = []
    
    # Iterate over each set of roads
    for i in range(num_sets):
        # Convert the current set of roads to a binary string
        binary_string = bin(i)[2:]
        binary_string = binary_string.zfill(n)
        
        # Check if the current set of roads forms a directed cycle
        if not is_confusing(n, roads, binary_string):
            # If it doesn't form a directed cycle, add it to the results list
            results.append(binary_string)
    
    # Return the number of possible sets of roads that can be flipped
    return len(results)

def f2(n, roads):
    # Calculate the number of possible sets of roads that can be flipped
    num_sets = (2**n) - 1
    
    # Initialize a list to store the results
    results = []
    
    # Iterate over each set of roads
    for i in range(num_sets):
        # Convert the current set of roads to a binary string
        binary_string = bin(i)[2:]
        binary_string = binary_string.zfill(n)
        
        # Check if the current set of roads forms a directed cycle
        if not is_confusing(n, roads, binary_string):
            # If it doesn't form a directed cycle, add it to the results list
            results.append(binary_string)
    
    # Return the number of possible sets of roads that can be flipped
    return len(results)

def is_confusing(n, roads, binary_string):
    # Initialize a list to store the visited towns
    visited = [False] * (n + 1)
    
    # Initialize a variable to store the current town
    current_town = 1
    
    # Iterate over each bit in the binary string
    for i in range(n):
        # If the current bit is 1, flip the road
        if binary_string[i] == "1":
            # Flip the road
            roads[i] = (roads[i] + 1) % n
        
        # Move to the next town
        current_town = roads[current_town - 1]
        
        # Mark the current town as visited
        visited[current_town] = True
    
    # Check if all towns have been visited
    if all(visited):
        return False
    else:
        return True

if __name__ == '__main__':
    n = int(input())
    roads = list(map(int, input().split()))
    print(f1(n, roads))
    print(f2(n, roads))

