
def calculate_distance(x1, y1, x2, y2):
    return ((x2-x1)**2 + (y2-y1)**2)**0.5

def solve(n, l, w, positions):
    # Sort the positions of the trees
    sorted_positions = sorted(positions)

    # Initialize the total distance to 0
    total_distance = 0

    # Loop through the positions of the trees
    for i in range(n):
        # Calculate the distance between the current tree and the next tree
        distance = calculate_distance(sorted_positions[i], 0, sorted_positions[i+1], 0)

        # Add the distance to the total distance
        total_distance += distance

    # Return the total distance
    return total_distance

def main():
    n, l, w = map(int, input().split())
    positions = []
    for _ in range(n):
        positions.append(int(input()))
    print(solve(n, l, w, positions))

if __name__ == '__main__':
    main()

