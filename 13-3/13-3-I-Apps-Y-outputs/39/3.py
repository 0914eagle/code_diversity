
def get_min_unlikeliness_tree(samples):
    # Initialize the unlikeliness of each edge as infinity
    unlikeliness = [[float('inf') for _ in range(len(samples))] for _ in range(len(samples))]

    # Compute the unlikeliness of each edge
    for i in range(len(samples)):
        for j in range(i+1, len(samples)):
            unlikeliness[i][j] = get_unlikeliness(samples[i], samples[j])

    # Fill in the unlikeliness matrix
    for k in range(len(samples)):
        for i in range(len(samples)):
            for j in range(len(samples)):
                unlikeliness[i][j] = min(unlikeliness[i][j], unlikeliness[i][k] + unlikeliness[k][j])

    # Find the minimum unlikeliness tree
    min_unlikeliness = float('inf')
    min_tree = []
    for i in range(len(samples)):
        for j in range(i+1, len(samples)):
            if unlikeliness[i][j] < min_unlikeliness:
                min_unlikeliness = unlikeliness[i][j]
                min_tree = [(i, j)]
            elif unlikeliness[i][j] == min_unlikeliness:
                min_tree.append((i, j))

    return min_unlikeliness, min_tree

def get_unlikeliness(s1, s2):
    # Compute the number of positions at which the two strings differ
    diff = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            diff += 1

    return diff

def main():
    samples = []
    for _ in range(int(input())):
        samples.append(input())
    min_unlikeliness, min_tree = get_min_unlikeliness_tree(samples)
    print(min_unlikeliness)
    for edge in min_tree:
        print(edge[0], edge[1])

if __name__ == "__main__":
    main()

