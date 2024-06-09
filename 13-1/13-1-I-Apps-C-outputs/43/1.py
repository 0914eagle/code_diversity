
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
            controlled_areas[i] = tree[i][0]
        if tree[i][1] == 'G':
            giant_birds.add(i)
        elif tree[i][1] == 'T':
            tiny_birds.add(i)
        elif tree[i][1] == 'E':
            elderberries.add(i)
            labels[i] = tree[i][2]

    # Determine the controlled areas of the tiny birds
    for i in tiny_birds:
        controlled_areas[i] = find_closest_big_branch(i, controlled_areas)

    # Determine which bird eats which berry
    for i in elderberries:
        bird = find_bird(i, labels, controlled_areas)
        berries[i] = bird

    # Change the labels of the tiny birds to make them giant birds
    for i in tiny_birds:
        labels[i] = labels[controlled_areas[i]]

    # Determine the minimum number of labels that need to be changed
    k = 0
    for i in elderberries:
        if berries[i] != find_bird(i, labels, controlled_areas):
            k += 1

    # Return the minimum number of labels that need to be changed and the labels that need to be changed
    return k, [i for i in labels if labels[i] != find_bird(i, labels, controlled_areas)]

def find_closest_big_branch(i, controlled_areas):
    # Find the closest big branch to vertex i
    while controlled_areas[i] not in giant_birds:
        i = controlled_areas[i]
    return controlled_areas[i]

def find_bird(i, labels, controlled_areas):
    # Find the bird that eats the berry at vertex i
    for j in controlled_areas[i]:
        if labels[j] == labels[i]:
            return j
    return None

