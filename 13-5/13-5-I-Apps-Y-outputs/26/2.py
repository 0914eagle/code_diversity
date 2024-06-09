
def get_shortest_path(packages):
    # Initialize the shortest path as empty string
    shortest_path = ""
    
    # Loop through the packages and calculate the minimum number of moves required to collect them
    for package in packages:
        # Calculate the number of moves required to collect the package
        moves = abs(package[0]) + abs(package[1])
        
        # If the number of moves is less than the current shortest path, update the shortest path
        if len(shortest_path) == 0 or len(shortest_path) > moves:
            shortest_path = "R" * package[0] + "U" * package[1]
    
    return shortest_path

def main():
    # Read the number of test cases
    num_test_cases = int(input())
    
    # Loop through the test cases
    for _ in range(num_test_cases):
        # Read the number of packages
        num_packages = int(input())
        
        # Initialize the packages list
        packages = []
        
        # Loop through the packages and read their coordinates
        for _ in range(num_packages):
            x, y = map(int, input().split())
            packages.append((x, y))
        
        # Get the shortest path to collect all the packages
        shortest_path = get_shortest_path(packages)
        
        # Print the result
        if len(shortest_path) == 0:
            print("NO")
        else:
            print("YES")
            print(shortest_path)

if __name__ == '__main__':
    main()

