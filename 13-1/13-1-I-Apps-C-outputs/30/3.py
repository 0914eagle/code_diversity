
def f1(m, n, islands):
    # Initialize a dictionary to store the number of Zax and Xaz on each island
    zax_count = {i: 0 for i in range(1, m + 1)}
    xaz_count = {i: 0 for i in range(1, m + 1)}

    # Iterate through the input and count the number of Zax and Xaz on each island
    for island in islands:
        if island[0] != 0:
            zax_count[island[0]] += 1
        if island[-1] != 0:
            xaz_count[island[-1]] += 1

    # Check if the number of Zax and Xaz on each island is equal
    for i in range(1, m + 1):
        if zax_count[i] != xaz_count[i]:
            return "NO"

    return "YES"

def f2(m, n, islands):
    # Initialize a set to store the natural resources present on each island
    resources = set()

    # Iterate through the input and add the natural resources present on each island to the set
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
    islands = [list(map(int, input().split())) for _ in range(m)]
    print(f1(m, n, islands))
    print(f2(m, n, islands))

