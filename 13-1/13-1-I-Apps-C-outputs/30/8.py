
def f1(m, n, islands):
    # Initialize a dictionary to store the number of occurrences of each resource
    resource_counts = {}
    for i in range(1, n+1):
        resource_counts[i] = 0
    
    # Iterate through the islands and count the number of occurrences of each resource
    for island in islands:
        for resource in island:
            if resource != 0:
                resource_counts[resource] += 1
    
    # Check if each resource is present on at least two islands
    for resource, count in resource_counts.items():
        if count < 2:
            return "NO"
    
    return "YES"

def f2(m, n, islands):
    # Initialize a dictionary to store the number of Zax and Xaz on each island
    island_counts = {}
    for i in range(m):
        island_counts[i] = [0, 0]
    
    # Iterate through the islands and count the number of Zax and Xaz on each island
    for i, island in enumerate(islands):
        for resource in island:
            if resource != 0:
                island_counts[i][resource-1] += 1
    
    # Check if each island has at least one Zax and one Xaz
    for island, counts in island_counts.items():
        if counts[0] == 0 or counts[1] == 0:
            return "NO"
    
    return "YES"

if __name__ == '__main__':
    m, n = map(int, input().split())
    islands = [list(map(int, input().split())) for _ in range(m)]
    print(f1(m, n, islands))
    print(f2(m, n, islands))

