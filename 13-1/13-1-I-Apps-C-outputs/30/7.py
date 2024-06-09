
def f1(m, n):
    # Initialize a list to store the number of islands with each resource
    num_islands_with_resource = [0] * (n + 1)
    
    # Iterate through each island
    for i in range(m):
        # Iterate through each resource on the current island
        for resource in range(1, n + 1):
            # If the resource is present on the current island, increment the count for that resource
            if resource in input():
                num_islands_with_resource[resource] += 1
    
    # Check if there are at least 2 islands with each resource
    for resource in range(1, n + 1):
        if num_islands_with_resource[resource] < 2:
            return "NO"
    
    return "YES"

def f2(...):
    # Implement f2 here
    pass

if __name__ == '__main__':
    m, n = map(int, input().split())
    print(f1(m, n))

