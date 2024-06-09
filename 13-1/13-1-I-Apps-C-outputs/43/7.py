
def solve(n, tree):
    # Initialize variables
    labels = {}
    controlled_areas = {}
    berries = {}
    giant_birds = set()
    tiny_birds = set()
    elderberries = set()

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
                elif tree[i][2] == 'E':
                    elderberries.add(i)
        else:
            controlled_areas[i] = i

    # Find the smallest controlled area for each tiny bird
    for bird in tiny_birds:
        smallest_area = float('inf')
        for area in controlled_areas:
            if area in giant_birds:
                continue
            if controlled_areas[area] == controlled_areas[bird]:
                smallest_area = min(smallest_area, controlled_areas[area])
        controlled_areas[bird] = smallest_area

    # Find the smallest controlled area for each elderberry
    for berry in elderberries:
        smallest_area = float('inf')
        for area in controlled_areas:
            if controlled_areas[area] == controlled_areas[berry]:
                smallest_area = min(smallest_area, controlled_areas[area])
        controlled_areas[berry] = smallest_area

    # Find the labels for each bird and berry
    for bird in giant_birds | tiny_birds | elderberries:
        labels[bird] = labels[controlled_areas[bird]]

    # Find the changes needed
    changes = []
    for bird in tiny_birds:
        if labels[bird] != labels[controlled_areas[bird]]:
            changes.append((bird, labels[controlled_areas[bird]]))
    for berry in elderberries:
        if labels[berry] != labels[controlled_areas[berry]]:
            changes.append((berry, labels[controlled_areas[berry]]))

    # Return the result
    return len(changes), changes

