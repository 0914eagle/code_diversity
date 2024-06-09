
def f1(m, n):
    # Initialize a list to store the natural resources present on each island
    natural_resources = []
    for i in range(m):
        natural_resources.append([])

    # Read the input and store the natural resources present on each island
    for i in range(m):
        resources = list(map(int, input().split()))
        for resource in resources:
            if resource != 0:
                natural_resources[i].append(resource)

    # Check if each natural resource is present on at least two islands
    for i in range(1, n + 1):
        count = 0
        for j in range(m):
            if i in natural_resources[j]:
                count += 1
        if count < 2:
            return "NO"

    # Check if each island has at least one natural resource
    for i in range(m):
        if len(natural_resources[i]) == 0:
            return "NO"

    return "YES"

def f2(...):
    # Implement f2 here
    pass

if __name__ == '__main__':
    m, n = map(int, input().split())
    print(f1(m, n))

