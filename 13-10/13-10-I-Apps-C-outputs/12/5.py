
def read_input():
    N = int(input())
    L, W = map(int, input().split())
    positions = []
    for _ in range(N):
        positions.append(int(input()))
    return N, L, W, positions

def move_trees(N, L, W, positions):
    # Calculate the minimum distance needed to move the trees
    min_distance = 0
    for i in range(N):
        tree_position = positions[i]
        tree_pair_position = tree_position + W / 2
        distance = abs(tree_pair_position - L / 2)
        min_distance += distance
    
    return min_distance

def main():
    N, L, W, positions = read_input()
    print(move_trees(N, L, W, positions))

if __name__ == '__main__':
    main()

