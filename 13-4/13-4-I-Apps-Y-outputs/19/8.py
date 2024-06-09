
import sys
input = sys.stdin.read()

# Function to calculate the Manhattan distance between two points
def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

# Function to find the nearest safe house to a given spy
def find_nearest_safe_house(spy, safe_houses):
    min_distance = float('inf')
    nearest_safe_house = None
    for safe_house in safe_houses:
        distance = manhattan_distance(spy, safe_house)
        if distance < min_distance:
            min_distance = distance
            nearest_safe_house = safe_house
    return nearest_safe_house

# Function to find the maximum Manhattan distance of any spy to a nearest safe house
def find_max_manhattan_distance(spies, safe_houses):
    max_distance = 0
    for spy in spies:
        nearest_safe_house = find_nearest_safe_house(spy, safe_houses)
        distance = manhattan_distance(spy, nearest_safe_house)
        if distance > max_distance:
            max_distance = distance
    return max_distance

# Main function
def main():
    # Read the input
    width, height = map(int, input().split())
    grid = []
    for _ in range(height):
        grid.append(list(input().strip()))

    # Find the spies and safe houses
    spies = []
    safe_houses = []
    for i in range(height):
        for j in range(width):
            if grid[i][j] == 'S':
                safe_houses.append((j, i))
            elif grid[i][j] == 'S':
                spies.append((j, i))

    # Find the maximum Manhattan distance
    max_distance = find_max_manhattan_distance(spies, safe_houses)

    # Print the result
    print(max_distance)

if __name__ == '__main__':
    main()

