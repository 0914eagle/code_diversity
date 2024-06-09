
import itertools

def get_expected_length(n, roads):
    # Initialize a dictionary to store the expected length for each city
    expected_length = {i: 0 for i in range(1, n + 1)}
    
    # Iterate over each road
    for u, v in roads:
        # Update the expected length for the two cities connected by the road
        expected_length[u] += 1
        expected_length[v] += 1
    
    # Return the expected length for the first city
    return expected_length[1]

def get_all_paths(n, roads):
    # Initialize a list to store all possible paths
    all_paths = []
    
    # Iterate over each road
    for u, v in roads:
        # Add the path from city u to city v to the list of all paths
        all_paths.append([u, v])
    
    # Return the list of all paths
    return all_paths

def get_expected_length_paths(n, roads):
    # Get all possible paths
    all_paths = get_all_paths(n, roads)
    
    # Initialize a dictionary to store the expected length for each path
    expected_length_paths = {path: 0 for path in all_paths}
    
    # Iterate over each road
    for u, v in roads:
        # Update the expected length for each path that goes through the road
        for path in all_paths:
            if u in path and v in path:
                expected_length_paths[path] += 1
    
    # Return the dictionary of expected lengths for each path
    return expected_length_paths

def get_expected_length_paths_recursive(n, roads, path):
    # If the path is empty, return 0
    if not path:
        return 0
    
    # If the path has only one city, return the expected length for that city
    if len(path) == 1:
        return expected_length_paths[path[0]]
    
    # If the path has more than one city, return the expected length for the path
    return sum(expected_length_paths[path[i:i+2]] for i in range(len(path) - 1))

def get_expected_length_paths_iterative(n, roads):
    # Initialize a dictionary to store the expected length for each path
    expected_length_paths = {path: 0 for path in all_paths}
    
    # Iterate over each road
    for u, v in roads:
        # Update the expected length for each path that goes through the road
        for path in all_paths:
            if u in path and v in path:
                expected_length_paths[path] += 1
    
    # Return the dictionary of expected lengths for each path
    return expected_length_paths

def main():
    # Read the input
    n = int(input())
    roads = []
    for _ in range(n - 1):
        u, v = map(int, input().split())
        roads.append([u, v])
    
    # Get the expected length of the journey
    expected_length = get_expected_length(n, roads)
    
    # Print the expected length of the journey
    print(expected_length)

if __name__ == '__main__':
    main()

