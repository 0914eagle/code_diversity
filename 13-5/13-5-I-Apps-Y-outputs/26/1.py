
def get_shortest_path(packages):
    # Initialize the shortest path as empty string
    shortest_path = ""
    
    # Loop through the packages and find the package with the minimum x-coordinate
    min_x = float('inf')
    for package in packages:
        if package[0] < min_x:
            min_x = package[0]
            min_package = package
    
    # Add the move to collect the minimum package to the shortest path
    shortest_path += "R" * (min_package[0] - 1) + "U" * (min_package[1] - 1)
    
    # Remove the collected package from the list
    packages.remove(min_package)
    
    # Loop through the remaining packages
    for package in packages:
        # Find the move that takes the robot to the package with the minimum manhattan distance from the current position
        min_distance = float('inf')
        for move in ["R", "U"]:
            new_position = (0, 0)
            if move == "R":
                new_position = (1, 0)
            else:
                new_position = (0, 1)
            distance = abs(package[0] - new_position[0]) + abs(package[1] - new_position[1])
            if distance < min_distance:
                min_distance = distance
                min_move = move
        
        # Add the move to the shortest path
        shortest_path += min_move
    
    return shortest_path

def main():
    tests = int(input())
    for test in range(tests):
        n = int(input())
        packages = []
        for package in range(n):
            x, y = map(int, input().split())
            packages.append((x, y))
        shortest_path = get_shortest_path(packages)
        if shortest_path:
            print("YES")
            print(shortest_path)
        else:
            print("NO")

if __name__ == '__main__':
    main()

