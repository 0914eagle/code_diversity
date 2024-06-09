
def get_shortest_path(packages):
    # Initialize the shortest path as an empty string
    shortest_path = ""
    
    # Loop through the packages and check if the current package is at a higher x-coordinate or y-coordinate than the previous package
    for i in range(len(packages) - 1):
        current_package = packages[i]
        next_package = packages[i + 1]
        if current_package[0] < next_package[0]:
            shortest_path += "R"
        elif current_package[1] < next_package[1]:
            shortest_path += "U"
    
    # Return the shortest path
    return shortest_path

def main():
    # Read the number of test cases
    num_test_cases = int(input())
    
    # Loop through the test cases
    for _ in range(num_test_cases):
        # Read the number of packages
        num_packages = int(input())
        
        # Read the packages
        packages = []
        for _ in range(num_packages):
            x, y = map(int, input().split())
            packages.append((x, y))
        
        # Get the shortest path
        shortest_path = get_shortest_path(packages)
        
        # Print the answer
        print("YES")
        print(shortest_path)

if __name__ == '__main__':
    main()

