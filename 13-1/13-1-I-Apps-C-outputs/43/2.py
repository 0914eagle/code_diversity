
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

    # Find the minimum number of labels to change
    min_labels = float('inf')
    for i in range(1, n+1):
        if i in tiny_birds and i not in giant_birds:
            # Find the smallest controlled area among all giant birds
            smallest_area = float('inf')
            for j in giant_birds:
                if controlled_areas[j] < smallest_area:
                    smallest_area = controlled_areas[j]

            # Find the smallest controlled area among all tiny birds
            smallest_area_tiny = float('inf')
            for j in tiny_birds:
                if controlled_areas[j] < smallest_area_tiny:
                    smallest_area_tiny = controlled_areas[j]

            # If the smallest controlled area among all giant birds is smaller than the smallest controlled area among all tiny birds, change the label of the bird at vertex i
            if smallest_area < smallest_area_tiny:
                min_labels = 1
                labels[i] = 'c'

    # Find the labels to change
    labels_to_change = []
    for i in range(1, n+1):
        if i in tiny_birds and i not in giant_birds and labels[i] == 'c':
            labels_to_change.append(i)

    # Return the minimum number of labels to change and the labels to change
    return [min_labels, labels_to_change]

