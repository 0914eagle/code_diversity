
def solve(n, tree):
    # Initialize variables
    labels = {}
    controlled_areas = {}
    berries = {}
    giant_birds = set()
    tiny_birds = set()

    # Parse the input tree
    for i in range(1, n+1):
        if tree[i][0] != 0:
            parent = tree[i][0]
            if tree[i][1] == 'B':
                controlled_areas[i] = parent
            elif tree[i][1] == 'S':
                labels[i] = tree[i][2]
                if tree[i][2] == 'G':
                    giant_birds.add(i)
                elif tree[i][2] == 'T':
                    tiny_birds.add(i)
            elif tree[i][1] == 'E':
                berries[i] = tree[i][2]

    # Find the controlled areas of the tiny birds
    for i in tiny_birds:
        controlled_areas[i] = find_controlled_area(i, controlled_areas)

    # Find the berries that need to be changed
    berries_to_change = set()
    for i in berries:
        if berries[i] in giant_birds and controlled_areas[i] in giant_birds:
            berries_to_change.add(i)

    # Find the labels that need to be changed
    labels_to_change = set()
    for i in berries_to_change:
        labels_to_change.add(labels[i])

    # Return the minimum number of labels to change
    return len(labels_to_change)

def find_controlled_area(i, controlled_areas):
    # Find the closest ancestor that is a big branch
    ancestor = controlled_areas[i]
    while ancestor != 0 and controlled_areas[ancestor] != 0:
        ancestor = controlled_areas[ancestor]
    return ancestor

