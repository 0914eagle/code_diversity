
def read_input():
    N = int(input())
    L, W = map(int, input().split())
    tree_positions = []
    for _ in range(N):
        tree_positions.append(int(input()))
    return N, L, W, tree_positions

def get_pair_distance(tree_positions, i):
    # Calculate the distance between the ith tree and its pair tree
    pair_tree_pos = (L - tree_positions[i]) // 2
    return abs(pair_tree_pos - tree_positions[i])

def get_total_distance(tree_positions):
    # Calculate the total distance needed to move the trees to their correct positions
    total_distance = 0
    for i in range(len(tree_positions)):
        total_distance += get_pair_distance(tree_positions, i)
    return total_distance

def get_optimal_pairing(tree_positions):
    # Find the optimal pairing of the trees with the minimum total distance
    optimal_pairing = []
    for i in range(len(tree_positions)):
        optimal_pairing.append((i, get_pair_distance(tree_positions, i)))
    optimal_pairing.sort(key=lambda x: x[1])
    return [i[0] for i in optimal_pairing]

def main():
    N, L, W, tree_positions = read_input()
    optimal_pairing = get_optimal_pairing(tree_positions)
    total_distance = get_total_distance(tree_positions)
    print(total_distance)

if __name__ == '__main__':
    main()

