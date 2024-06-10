
def get_distance(x1, y1, x2, y2):
    return ((x2-x1)**2 + (y2-y1)**2)**0.5

def solve(N, L, W, tree_positions):
    # Sort the tree positions in ascending order
    tree_positions.sort()

    # Initialize the total distance to move the trees
    total_distance = 0

    # Loop through the tree positions and calculate the distance to move each tree
    for i in range(N-1):
        x1 = tree_positions[i]
        x2 = tree_positions[i+1]
        y1 = W/2
        y2 = W/2
        distance = get_distance(x1, y1, x2, y2)
        total_distance += distance

    return total_distance

def main():
    N, L, W = map(int, input().split())
    tree_positions = []
    for _ in range(N):
        tree_positions.append(int(input()))
    print(solve(N, L, W, tree_positions))

if __name__ == '__main__':
    main()

