
def get_shortest_path(packages):
    # Initialize the shortest path as empty string
    shortest_path = ""
    
    # Sort the packages by their x-coordinate in ascending order
    sorted_packages = sorted(packages, key=lambda x: x[0])
    
    # Iterate through the packages and add "R" to the shortest path for each package on the right side
    for package in sorted_packages:
        shortest_path += "R"
    
    # Add "U" to the shortest path for each package on the upper side
    for package in sorted_packages:
        shortest_path += "U"
    
    return shortest_path

def main():
    test_cases = int(input())
    for _ in range(test_cases):
        n = int(input())
        packages = []
        for _ in range(n):
            x, y = map(int, input().split())
            packages.append((x, y))
        shortest_path = get_shortest_path(packages)
        print("YES")
        print(shortest_path)

if __name__ == '__main__':
    main()

