
def get_distance(x1, y1, x2, y2):
    return ((x2-x1)**2 + (y2-y1)**2)**0.5

def arrange_trees(N, L, W, positions):
    # Sort the positions of the trees
    sorted_positions = sorted(positions)

    # Initialize the distance traveled to 0
    distance = 0

    # Loop through the positions of the trees
    for i in range(N):
        # Calculate the position of the current tree on the right side of the road
        right_position = L - sorted_positions[i]

        # Calculate the distance between the current tree and its corresponding tree on the right side of the road
        distance += get_distance(sorted_positions[i], 0, right_position, W)

    return distance

def main():
    N, L, W = map(int, input().split())
    positions = []
    for _ in range(N):
        positions.append(int(input()))
    print(arrange_trees(N, L, W, positions))

if __name__ == '__main__':
    main()

