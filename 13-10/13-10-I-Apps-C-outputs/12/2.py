
def read_input():
    N = int(input())
    L, W = map(int, input().split())
    positions = []
    for _ in range(N):
        positions.append(int(input()))
    return N, L, W, positions

def align_trees(N, L, W, positions):
    # Initialize the tree pairs and their positions
    tree_pairs = [(positions[i], positions[i+1]) for i in range(0, N, 2)]
    tree_positions = [(L/2 - W/2, L/2 + W/2)]
    
    # Iterate through the tree pairs and update their positions
    for pair in tree_pairs:
        pair_positions = []
        for tree in pair:
            pair_positions.append(tree_positions[0][0] + tree)
        tree_positions.append((pair_positions[0], pair_positions[1]))
    
    # Calculate the total distance moved
    total_distance = 0
    for i in range(N):
        total_distance += abs(tree_positions[i][0] - positions[i])
    
    return total_distance

def main():
    N, L, W, positions = read_input()
    print(align_trees(N, L, W, positions))

if __name__ == '__main__':
    main()

