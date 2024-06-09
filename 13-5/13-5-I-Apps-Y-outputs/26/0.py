
def get_shortest_path(packages):
    # Initialize the shortest path as empty string
    shortest_path = ""
    
    # Loop through the packages and calculate the minimum number of moves required to collect them
    for package in packages:
        # Calculate the number of moves required to collect the current package
        moves = calculate_moves(package)
        
        # If the current package requires more moves than the shortest path, skip it
        if moves > len(shortest_path):
            continue
        
        # If the current package requires the same number of moves as the shortest path, check if the current path is lexicographically smaller
        if moves == len(shortest_path):
            if shortest_path > get_path_string(package):
                continue
        
        # If the current package is the shortest path, update the shortest path
        shortest_path = get_path_string(package)
    
    # Return the shortest path
    return shortest_path

def calculate_moves(package):
    # Calculate the number of moves required to collect the package
    x, y = package
    return abs(x) + abs(y)

def get_path_string(package):
    # Get the path string for the package
    x, y = package
    path = ""
    if x > 0:
        path += "R" * x
    if y > 0:
        path += "U" * y
    return path

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
        if shortest_path == "":
            print("NO")
        else:
            print("YES")
            print(shortest_path)

if __name__ == '__main__':
    main()

