
def get_minimal_unlikeliness_tree(samples):
    # Initialize the tree with a single node for each sample
    tree = {i: [i] for i in range(len(samples))}
    # Iterate over the samples and find the most likely parent for each sample
    for i in range(len(samples)):
        parent = None
        min_distance = float('inf')
        for j in range(len(samples)):
            if i != j:
                distance = get_distance(samples[i], samples[j])
                if distance < min_distance:
                    min_distance = distance
                    parent = j
        # Add the edge between the parent and the current sample to the tree
        tree[parent].append(i)
    # Calculate the unlikeliness of the tree
    unlikeliness = 0
    for node in tree.values():
        for child in node:
            unlikeliness += get_distance(samples[node[0]], samples[child])
    return unlikeliness, tree

def get_distance(s1, s2):
    return sum(c1 != c2 for c1, c2 in zip(s1, s2))

def get_edges(tree):
    edges = []
    for parent, children in tree.items():
        for child in children:
            edges.append((parent, child))
    return edges

def main():
    samples = []
    for _ in range(int(input())):
        samples.append(input())
    unlikeliness, tree = get_minimal_unlikeliness_tree(samples)
    print(unlikeliness)
    for edge in get_edges(tree):
        print(*edge)

if __name__ == '__main__':
    main()

