
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
            # Find the smallest controlled area among all giant birds that can eat the berry at vertex i
            min_area = float('inf')
            for j in giant_birds:
                if berries[i] == labels[j] and controlled_areas[j] < min_area:
                    min_area = controlled_areas[j]

            # Find the smallest controlled area among all tiny birds that can eat the berry at vertex i
            min_area_tiny = float('inf')
            for j in tiny_birds:
                if berries[i] == labels[j] and controlled_areas[j] < min_area_tiny:
                    min_area_tiny = controlled_areas[j]

            # Update the minimum number of labels to change
            if min_area < min_area_tiny:
                min_labels = min(min_labels, min_area - controlled_areas[i])
            else:
                min_labels = min(min_labels, min_area_tiny - controlled_areas[i])

    # Find the labels to change
    labels_to_change = []
    for i in range(1, n+1):
        if i in tiny_birds and i not in giant_birds:
            # Find the smallest controlled area among all giant birds that can eat the berry at vertex i
            min_area = float('inf')
            for j in giant_birds:
                if berries[i] == labels[j] and controlled_areas[j] < min_area:
                    min_area = controlled_areas[j]

            # Find the smallest controlled area among all tiny birds that can eat the berry at vertex i
            min_area_tiny = float('inf')
            for j in tiny_birds:
                if berries[i] == labels[j] and controlled_areas[j] < min_area_tiny:
                    min_area_tiny = controlled_areas[j]

            # Update the labels to change
            if min_area < min_area_tiny:
                labels_to_change.append((i, min_area))
            else:
                labels_to_change.append((i, min_area_tiny))

    # Sort the labels to change by their controlled area
    labels_to_change.sort(key=lambda x: x[1])

    # Return the minimum number of labels to change and the labels to change
    return (min_labels, labels_to_change)

