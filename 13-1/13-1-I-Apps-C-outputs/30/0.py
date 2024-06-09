
def f1(m, n, islands):
    # Initialize a dictionary to store the number of Zax and Xaz on each island
    zax_count = {i: 0 for i in range(1, m + 1)}
    xaz_count = {i: 0 for i in range(1, m + 1)}

    # Iterate through the input islands and count the number of Zax and Xaz on each island
    for island in islands:
        for resource in island:
            if resource != 0:
                if resource % 2 == 0:
                    zax_count[island[0]] += 1
                else:
                    xaz_count[island[0]] += 1

    # Check if the number of Zax and Xaz on each island is equal
    for island in range(1, m + 1):
        if zax_count[island] != xaz_count[island]:
            return "NO"

    return "YES"

def f2(m, n, islands):
    # Initialize a set to store the natural resources present on each island
    resources = set()

    # Iterate through the input islands and add the natural resources to the set
    for island in islands:
        for resource in island:
            if resource != 0:
                resources.add(resource)

    # Check if the set of natural resources is equal to the number of natural resources
    if len(resources) == n:
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    m, n = map(int, input().split())
    islands = []
    for _ in range(m):
        island = list(map(int, input().split()))
        islands.append(island)
    print(f1(m, n, islands))
    print(f2(m, n, islands))

