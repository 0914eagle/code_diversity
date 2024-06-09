
def get_maximum_types(n, m, a, k):
    # Sort the list of already owned toys in ascending order
    a.sort()
    # Initialize variables to keep track of the number of types and cost
    num_types = 0
    cost = 0
    # Iterate through the list of already owned toys
    for i in range(n):
        # If the current toy is not already owned, add it to the list of types and increase the cost
        if a[i] not in a[:i]:
            num_types += 1
            cost += a[i]
        # If the cost exceeds the given limit, return the current number of types and list of types
        if cost > m:
            return num_types, a[:i]
    # If all toys have been iterated through and the cost is still within limit, return the current number of types and list of types
    return num_types, a


n, m = map(int, input().split())
a = list(map(int, input().split()))
k, b = get_maximum_types(n, m, a, k)
print(k)
print(*b)

