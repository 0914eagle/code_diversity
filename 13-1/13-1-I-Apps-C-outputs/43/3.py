
def solve(n, tree):
    # Initialize variables
    labels = {}
    controlled_areas = {}
    berries = {}
    giant_birds = []
    tiny_birds = []
    elderberries = []

    # Parse the input tree
    for i in range(1, n+1):
        if tree[i][0] != 0:
            controlled_areas[i] = tree[i][0]
        if tree[i][1] == 'G':
            giant_birds.append(i)
        elif tree[i][1] == 'T':
            tiny_birds.append(i)
        elif tree[i][1] == 'E':
            elderberries.append(i)
            labels[i] = tree[i][2]

    # Determine the controlled areas of the tiny birds
    for i in tiny_birds:
        controlled_areas[i] = find_controlled_area(i, controlled_areas)

    # Determine which bird eats which berry
    for i in elderberries:
        bird = find_bird(i, labels, controlled_areas)
        berries[i] = bird

    # Change the labels of the tiny birds to make them giant birds
    for i in tiny_birds:
        labels[i] = 'G'

    # Determine the controlled areas of the giant birds
    for i in giant_birds:
        controlled_areas[i] = find_controlled_area(i, controlled_areas)

    # Determine which bird eats which berry after the labels are changed
    for i in elderberries:
        bird = find_bird(i, labels, controlled_areas)
        if bird != berries[i]:
            return -1

    return 0

def find_controlled_area(i, controlled_areas):
    # Find the parent of the current vertex
    parent = controlled_areas[i]

    # If the parent is a big branch, return its controlled area
    if controlled_areas[parent] == 0:
        return parent

    # If the parent is a small branch, find the closest big branch
    while controlled_areas[parent] != 0:
        parent = controlled_areas[parent]

    return parent

def find_bird(i, labels, controlled_areas):
    # Find the bird with the same label as the current berry
    for bird in labels:
        if labels[bird] == labels[i]:
            # If the bird is inside the controlled area of the current berry, return it
            if controlled_areas[bird] == controlled_areas[i]:
                return bird

    return -1

