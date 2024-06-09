
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
            if bird in controlled_areas[area]:
                smallest_area = min(smallest_area, area)
        controlled_areas[bird] = smallest_area

    # Find the smallest controlled area for each giant bird
    for bird in giant_birds:
        smallest_area = float('inf')
        for area in controlled_areas:
            if bird in controlled_areas[area]:
                smallest_area = min(smallest_area, area)
        controlled_areas[bird] = smallest_area

    # Find the smallest controlled area for each elderberry
    for berry in elderberries:
        smallest_area = float('inf')
        for area in controlled_areas:
            if berry in controlled_areas[area]:
                smallest_area = min(smallest_area, area)
        controlled_areas[berry] = smallest_area

    # Find the labels for each bird and berry
    for bird in controlled_areas:
        if bird in giant_birds:
            labels[bird] = labels[controlled_areas[bird]]
        elif bird in tiny_birds:
            labels[bird] = labels[controlled_areas[bird]]
        elif bird in elderberries:
            labels[bird] = labels[controlled_areas[bird]]

    # Find the number of changes needed
    changes_needed = 0
    for bird in controlled_areas:
        if labels[bird] != labels[controlled_areas[bird]]:
            changes_needed += 1

    # Find the changes to be made
    changes = []
    for bird in controlled_areas:
        if labels[bird] != labels[controlled_areas[bird]]:
            changes.append((bird, labels[controlled_areas[bird]]))

    return changes_needed, changes

