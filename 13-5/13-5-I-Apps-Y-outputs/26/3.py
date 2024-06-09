
def get_shortest_path(packages):
    # Initialize the shortest path as an empty string
    shortest_path = ""
    
    # Loop through the packages and find the package that is farthest from the starting point (0, 0)
    for package in packages:
        # Calculate the distance between the package and the starting point
        distance = abs(package[0]) + abs(package[1])
        
        # If the distance is greater than the current shortest distance, update the shortest distance and the shortest path
        if distance > shortest_distance:
            shortest_distance = distance
            shortest_path = "U" * package[1] + "R" * package[0]
    
    # Return the shortest path
    return shortest_path

def main():
    # Read the number of test cases
    num_test_cases = int(input())
    
    # Loop through the test cases
    for _ in range(num_test_cases):
        # Read the number of packages
        num_packages = int(input())
        
        # Initialize the packages as a list of tuples (x, y)
        packages = [(0, 0)]
        
        # Loop through the packages and read their coordinates
        for _ in range(num_packages):
            x, y = map(int, input().split())
            packages.append((x, y))
        
        # Get the shortest path to collect all packages
        shortest_path = get_shortest_path(packages)
        
        # Print "YES" if the shortest path is not empty, otherwise print "NO"
        if shortest_path:
            print("YES")
            print(shortest_path)
        else:
            print("NO")

if __name__ == '__main__':
    main()

