
def get_connected_components(n, a):
    # Initialize a dictionary to map each district to its connected component
    connected_components = {}
    for i in range(n):
        connected_components[i] = i

    # Iterate over the districts and their gangs
    for i in range(n):
        for j in range(i+1, n):
            # If the districts belong to different gangs, connect them
            if a[i] != a[j]:
                connected_components[i] = j
                break

    # Find the connected components
    components = []
    for i in range(n):
        if connected_components[i] not in components:
            components.append(connected_components[i])

    return components

def get_minimum_roads(n, a):
    # Get the connected components
    components = get_connected_components(n, a)

    # If there is only one connected component, return -1
    if len(components) == 1:
        return -1

    # Initialize the minimum number of roads to be the number of connected components - 1
    minimum_roads = len(components) - 1

    # Iterate over the connected components
    for i in range(len(components)):
        # Get the current component
        component = components[i]

        # Iterate over the other connected components
        for j in range(i+1, len(components)):
            # If the current component and the other component have different gangs, add a road
            if a[component] != a[components[j]]:
                minimum_roads += 1

    return minimum_roads

def get_roads(n, a, minimum_roads):
    # Initialize the roads list
    roads = []

    # If the minimum number of roads is -1, return an empty list
    if minimum_roads == -1:
        return roads

    # Get the connected components
    components = get_connected_components(n, a)

    # Initialize a dictionary to map each district to its connected component
    connected_components = {}
    for i in range(n):
        connected_components[i] = components[0]

    # Iterate over the connected components
    for i in range(1, len(components)):
        # Get the current component
        component = components[i]

        # Iterate over the districts in the current component
        for j in range(n):
            # If the district is in the current component, add it to the list of roads
            if connected_components[j] == component:
                roads.append(j)

    # Shuffle the roads list
    import random
    random.shuffle(roads)

    # Return the first minimum_roads roads
    return roads[:minimum_roads]

def solve(n, a):
    # Get the minimum number of roads
    minimum_roads = get_minimum_roads(n, a)

    # Get the roads
    roads = get_roads(n, a, minimum_roads)

    # If there are no roads, return "NO"
    if not roads:
        return "NO"

    # Otherwise, return "YES" and the roads
    return "YES\n" + "\n".join(str(x+1) + " " + str(y+1) for x, y in zip(roads[::2], roads[1::2]))

if __name__ == '__main__':
    # Get the number of test cases
    t = int(input())

    # Iterate over the test cases
    for _ in range(t):
        # Get the number of districts and the gangs
        n = int(input())
        a = list(map(int, input().split()))

        # Solve the problem
        print(solve(n, a))

