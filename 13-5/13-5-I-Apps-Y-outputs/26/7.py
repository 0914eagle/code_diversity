
def get_shortest_path(packages):
    # Initialize the shortest path as empty string
    shortest_path = ""
    
    # Loop through the packages and add the appropriate move to the path
    for package in packages:
        # If the package is to the right of the current position, add a "R" to the path
        if package[0] > 0:
            shortest_path += "R"
        # If the package is above the current position, add a "U" to the path
        elif package[1] > 0:
            shortest_path += "U"
    
    return shortest_path

def main():
    # Read the number of test cases
    num_test_cases = int(input())
    
    # Loop through the test cases
    for _ in range(num_test_cases):
        # Read the number of packages
        num_packages = int(input())
        
        # Initialize the packages as a list of tuples (x, y)
        packages = []
        for _ in range(num_packages):
            x, y = map(int, input().split())
            packages.append((x, y))
        
        # Get the shortest path for the packages
        shortest_path = get_shortest_path(packages)
        
        # Print the answer
        print("YES")
        print(shortest_path)

if __name__ == '__main__':
    main()

